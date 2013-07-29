# -*- coding: utf-8 -*-
###################################################################################
# Added to enable code completion in IDE's.
if 0:
    import logger
###################################################################################
from gluon import current
from helper import get_config_file

def login_callback(form):
    if current.auth.is_logged_in():
        add_group_test()
    

def login_ldap_callback(form):
    if current.auth.is_logged_in():
        user_name = current.auth.user.username
        if current.db(current.db.user.username == user_name).select(current.db.user.last_name)[0]['last_name'] == "":             
            result = fetch_ldap_user(user_name)
            if result:
                create_or_update_user(user_name, result[0], result[1], result[2], result[3], result[4],True)
            else:
                current.logger.error('Unable To Update User Info!!!')

    
def add_group_test():

    config = get_config_file()
    _role = current.USER
    
    member = current.db(current.db.user_membership.user_id == current.auth.user.id).select().first()
    if not member:
        add_membership_db(current.auth.user.id, _role, True)


def fetch_ldap_user(username):
    config = get_config_file()
    ldap_url = config.get("LDAP_CONF","ldap_url")
    base_dn = config.get("LDAP_CONF","ldap_dn")

    import ldap
    try:
        l = ldap.open(ldap_url)
        l.protocol_version = ldap.VERSION3    
    except ldap.LDAPError, e:
        current.logger.error(e)
        return None

    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = None
    searchFilter = "uid="+username
    _first_name = ''
    _last_name = ''
    _email = None
    _role_list = [current.USER]
    _organisation = 'IIT Delhi'

    try:
        ldap_result_id = l.search(base_dn, searchScope, searchFilter, retrieveAttributes)  
        while 1:
            result_type, result_data = l.result(ldap_result_id, 0)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    for name,attrs in result_data:
                        for k,vals in attrs.items():
                            if k == 'cn':
                                name_lst = vals[0].split(' ')
                                _first_name = name_lst[0]
                                if len(name_lst) == 2:
                                    _last_name = name_lst[1]
                                else:
                                    _last_name = vals[0][vals[0].index(' '):].lstrip()
                            if k == 'altEmail':
                                if vals[0] != 'none':
                                    _email=vals[0]
 
#TODO: find role and organisation from ldap and set in db accordingly (current iitd ldap does not support this feature entirely) 
                                    
        admin_users = config.get("GENERAL_CONF","admin_uid")
        orgadmin_users = config.get("GENERAL_CONF","orgadmin_uid")        
        faculty_users = config.get("GENERAL_CONF","faculty_uid")

        if username in admin_users:
            _role_list.append(current.ADMIN)
        if username in orgadmin_users:
            _role_list.append(current.ORGADMIN)
        if username in faculty_users:
            _role_list.append(current.FACULTY)

    except ldap.LDAPError, e:
        current.logger.error(e)

    current.logger.info(str(_first_name)+" : "+str(_last_name)+" : "+str(_email)+" : "+str(_role_list)+" : "+str(_organisation))

    if _first_name and _last_name and _email and _organisation:
        return(_first_name, _last_name, _email, _role_list, _organisation)
    else: 
        return None

#This method is called only when user logs in for the first time or when faculty name is verified on 'request VM' screen
def create_or_update_user(user_name, first_name, last_name, email, roles, organisation, update_session):

    is_new_user = False
    user = current.db(current.db.user.username == user_name).select().first()
    
    if not user:
        #create user
        user = current.db.user.insert(username=user_name, registration_id=user_name)
        is_new_user = True
    
    org_id = current.db(organisation == current.db.organisation.name).select(current.db.organisation.id).first()    
    current.db(current.db.user.username==user_name).update(first_name = first_name, last_name = last_name, email = email, organisation_id = org_id)
                                                         
    add_or_update_user_memberships(user.id, is_new_user, roles, update_session)   


def add_or_update_user_memberships(user_id, new_user, roles, update_session):

    if not new_user:
        current_roles = current.db((user_id == current.db.user_membership.user_id) & (current.db.user_membership.group_id == current.db.user_group.id)).select(current.db.user_group.role).as_list()

        current.logger.info("users current roles: %s",current_roles)

        for role in current_roles:
            roles.pop(roles.index(role['role']))
        
    for role in roles:
        add_membership_db(user_id, role, update_session)


def add_membership_db(_user_id, role, update_session):
    #Find the group_id for the given role
    _group_id = current.db(current.db.user_group.role==role).select(current.db.user_group.id).first()['id']
    _org_id = current.db(current.db.user.id == _user_id).select(current.db.user.organisation_id).first()['organisation_id']
    if _group_id !=0:
        current.db.user_membership.insert(user_id=_user_id,group_id=_group_id)
        if update_session:
            # add role to the current session
            current.auth.user_groups[long(_group_id)] = role
            current.auth.organisation_id = _org_id
            current.logger.debug(_org_id)
            current.logger.debug(role)