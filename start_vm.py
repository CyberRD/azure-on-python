from azure import *
from azure.servicemanagement import *

subscription_id = 'd098e93b-c597-4bd5-9e17-11dbcee0d683'
certificate_path = 'CURRENT_USER\\my\\user-PC'

sms = ServiceManagementService(subscription_id, certificate_path)

service_name = 'gooooodnight1679'
vm_name = 'gooooodnight1679'

sms.start_role(service_name, vm_name, vm_name)