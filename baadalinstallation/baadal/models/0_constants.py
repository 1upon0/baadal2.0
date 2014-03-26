#Task Queue status
TASK_QUEUE_STATUS_PENDING = 1
TASK_QUEUE_STATUS_PROCESSING = 2
TASK_QUEUE_STATUS_SUCCESS = 3
TASK_QUEUE_STATUS_FAILED = 4
TASK_QUEUE_STATUS_RETRY = 5
TASK_QUEUE_STATUS_IGNORE = 6
TASK_QUEUE_STATUS_PARTIAL_SUCCESS = 7

from gluon import current
current.TASK_QUEUE_STATUS_SUCCESS = TASK_QUEUE_STATUS_SUCCESS
current.TASK_QUEUE_STATUS_FAILED = TASK_QUEUE_STATUS_FAILED

#Task type
TASK_TYPE_CREATE_VM = 'Create VM'
TASK_TYPE_MIGRATE_VM = 'Migrate VM'
TASK_TYPE_START_VM = 'Start VM'
TASK_TYPE_STOP_VM = 'Stop VM'
TASK_TYPE_SUSPEND_VM = 'Suspend VM'
TASK_TYPE_RESUME_VM = 'Resume VM'
TASK_TYPE_DELETE_VM = 'Delete VM'
TASK_TYPE_DESTROY_VM = 'Destroy VM'
TASK_TYPE_DELETE_SNAPSHOT = 'Delete Snapshot'
TASK_TYPE_REVERT_TO_SNAPSHOT = 'Revert to Snapshot'
TASK_TYPE_EDITCONFIG_VM = 'Edit VM Config'
TASK_TYPE_SNAPSHOT_VM = 'Snapshot VM'
TASK_TYPE_CLONE_VM = 'Clone VM'
TASK_TYPE_ATTACH_DISK = 'Attach Disk'

#Task Queue Priority
TASK_QUEUE_PRIORITY_LOW = 0
TASK_QUEUE_PRIORITY_NORMAL = 1
TASK_QUEUE_PRIORITY_HIGH = 2
TASK_QUEUE_PRIORITY_URGENT = 3

REQ_STATUS_REQUESTED = 1
REQ_STATUS_REJECTED  = 2
REQ_STATUS_VERIFIED  = 3
REQ_STATUS_APPROVED  = 4
REQ_STATUS_IN_QUEUE  = 5
REQ_STATUS_FAILED    =-1
#VM Status
VM_STATUS_UNKNOWN   =-1
VM_STATUS_IN_QUEUE  = 1
VM_STATUS_RUNNING   = 2
VM_STATUS_SUSPENDED = 3
VM_STATUS_SHUTDOWN  = 4

current.VM_STATUS_RUNNING = VM_STATUS_RUNNING
current.VM_STATUS_SUSPENDED = VM_STATUS_SUSPENDED
current.VM_STATUS_SHUTDOWN = VM_STATUS_SHUTDOWN
current.VM_STATUS_UNKNOWN = VM_STATUS_UNKNOWN
current.VM_STATUS_IN_QUEUE = VM_STATUS_IN_QUEUE

#NETWORK
LIBVIRT_NETWORK ='ovs-net'
current.LIBVIRT_NETWORK = LIBVIRT_NETWORK

#STORAGE
STORAGE_NETAPP_NFS = 'netapp_nfs'
STORAGE_LINUX_NFS = 'linux_nfs'

current.STORAGE_NETAPP_NFS = STORAGE_NETAPP_NFS
current.STORAGE_LINUX_NFS = STORAGE_LINUX_NFS

#SNAPSHOTTING LIMIT
SNAPSHOTTING_LIMIT = 3
SNAPSHOT_DAILY=1
SNAPSHOT_WEEKLY=2
SNAPSHOT_MONTHLY=3
SNAPSHOT_YEARLY=4
SNAPSHOT_USER=5
SNAPSHOT_SYSTEM=6
current.SNAPSHOT_USER=SNAPSHOT_USER
current.SNAPSHOT_SYSTEM=SNAPSHOT_SYSTEM

#User status
USER_PENDING_APPROVAL='pending'

ADMIN = 'admin'
ORGADMIN = 'orgadmin'
FACULTY = 'faculty'
USER = 'user'

current.ADMIN = ADMIN
current.ORGADMIN = ORGADMIN
current.FACULTY = FACULTY
current.USER = USER

PUBLIC_IP_NOT_ASSIGNED = "Not Assigned"
current.PUBLIC_IP_NOT_ASSIGNED = PUBLIC_IP_NOT_ASSIGNED

ITEMS_PER_PAGE=20

VM_RAM_SET = (256, 512,1024,2048,4096,8192)
VM_vCPU_SET = (1,2,4,8)

IP_ERROR_MESSAGE = 'Enter valid IP address'
NAME_ERROR_MESSAGE = 'Name should start with alphanumeric and can only contain letters, numbers, dash and underscore'
SECURITY_DOMAIN_DELETE_MESSAGE = 'There are VMs assigned to this security domain. It can''t be deleted.'
PRIVATE_IP_DELETE_MESSAGE = 'Private IP is assigned to a VM. It can''t be deleted.'

SECONDS = 1
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES
DAYS = 24 * HOURS

HOST_VLAN_ID=1

BAADAL_STATUS_UP='up'
BAADAL_STATUS_UP_IN_PROGRESS='up-progress'
BAADAL_STATUS_DOWN='down'
BAADAL_STATUS_DOWN_IN_PROGRESS='down-progress'

# List of valid CPU and RAM combination
VM_CONFIGURATION = [(1,0.25),(1,0.5),(1,1),(1,2),(2,2),(2,4),(4,4),(4,8),(8,8),(8,16)]

#Added so that changes in modules are instantlly loaded and reflected.
from gluon.custom_import import track_changes; track_changes(True)
