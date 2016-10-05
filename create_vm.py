from azure import *
from azure.servicemanagement import *

subscription_id = 'XXX'
certificate_path = 'CURRENT_USER\\my\\AzureCertificate'

sms = ServiceManagementService(subscription_id, certificate_path)

'''
images = sms.list_vm_images()
for image in images:
    print image.name
'''

service_name = 'marsTestClean1005'
image_name = 'Cybermars_Clean_Test_Env_HTTP'
vm_name = 'marsTestClean1005'
location = "Japan West"
virtual_network_name ="Group SDD SDD"

windows_config = WindowsConfigurationSet(computer_name="SDD",
    admin_username = "SDD",
    admin_password = "XXX",
    reset_password_on_first_logon = False,
    enable_automatic_updates  = False)
windows_config.domain_join = None
windows_config.win_rm.listeners.listeners.append(Listener('Https'))
windows_config.win_rm.listeners.listeners.append(Listener('Http'))

network_config = ConfigurationSet()
network_config.input_endpoints.input_endpoints.append(ConfigurationSetInputEndpoint(name='Remote Desktop',
                                                                                    protocol='TCP',
                                                                                    port='3389',
                                                                                    local_port='3389'))

network_config.input_endpoints.input_endpoints.append(ConfigurationSetInputEndpoint(name='WinRM',
                                                                                    protocol='TCP',
                                                                                    port='5986',
                                                                                    local_port='5986'))

network_config.input_endpoints.input_endpoints.append(ConfigurationSetInputEndpoint(name='WinRM_HTTP',
                                                                                    protocol='TCP',
                                                                                    port='5985',
                                                                                    local_port='5985'))

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
    role_size='Standard_DS2',
    vm_image_name = image_name,
    provision_guest_agent=True,
    network_config=network_config,
    virtual_network_name=virtual_network_name)
