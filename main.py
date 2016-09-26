from azure import *
from azure.servicemanagement import *

subscription_id = 'TEST'
certificate_path = 'CURRENT_USER\\my\\user-PC'

sms = ServiceManagementService(subscription_id, certificate_path)

'''
images = sms.list_vm_images()
for image in images:
    print image.name
'''

service_name = 'typhoon001wq'
image_name = 'testServerSource'
vm_name = 'typhoon001wq'
location = "Japan West"

windows_config = WindowsConfigurationSet(computer_name="SDD",
    admin_username = "TEST",
    admin_password = "TEST",
    reset_password_on_first_logon = False,
    enable_automatic_updates  = False)
windows_config.domain_join = None
windows_config.win_rm.listeners.listeners.append(Listener('Https'))

network_config = ConfigurationSet()
network_config.input_endpoints.input_endpoints.append(ConfigurationSetInputEndpoint(name='Remote Desktop',
                                                                                    protocol='TCP',
                                                                                    port='3389',
                                                                                    local_port='3389'))

network_config.input_endpoints.input_endpoints.append(ConfigurationSetInputEndpoint(name='WinRM',
                                                                                    protocol='TCP',
                                                                                    port='5986',
                                                                                    local_port='5986'))

#Set the location
sms.create_hosted_service(service_name=service_name,
    label=service_name,
    location=location)

sms.create_virtual_machine_deployment(service_name=service_name,
    deployment_name=vm_name,
    deployment_slot='production',
    label=vm_name,
    role_name=vm_name,
    system_config=windows_config,
    os_virtual_hard_disk=None,
    role_size='Standard_DS1_v2',
    vm_image_name = image_name,
    provision_guest_agent=True,
    network_config=network_config)
