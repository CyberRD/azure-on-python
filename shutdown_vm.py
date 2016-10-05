from azure import *
from azure.servicemanagement import *

subscription_id = 'XXX'
certificate_path = 'CURRENT_USER\\my\\AzureCertificate'

sms = ServiceManagementService(subscription_id, certificate_path)

service_name = 'gooooodnight1679'
vm_name = 'gooooodnight1679'

sms.shutdown_role(service_name, vm_name, vm_name)