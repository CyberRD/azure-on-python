from winrm.protocol import Protocol

p = Protocol(
    endpoint='https://typhoon12341015.cloudapp.net:5986/wsman',
    transport='ntlm',
    username=r'SDD',
    password='1qaz2wsx3edc!',
    server_cert_validation='ignore')
shell_id = p.open_shell()
command_id = p.run_command(shell_id, 'ipconfig', ['/all'])
std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
print std_out
print status_code
print std_err
p.cleanup_command(shell_id, command_id)
p.close_shell(shell_id)