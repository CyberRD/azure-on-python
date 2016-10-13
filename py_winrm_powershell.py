import winrm

ps_script = """
cd C:\chef-cybermars-test-auto-deploy\cookbooks
chef-client --local-mode --runlist 'recipe[cybermars_test_auto_deploy_simple]'
"""

'''
for 開發環境
cd C:\chef-cybermars-auto-deploy\cookbooks
chef-client --local-mode --runlist 'recipe[cybermars_auto_deploy_simple]'
'''

s = winrm.Session('http://marstestclean1012.cloudapp.net:5985/wsman', auth=('SDD', 'XXX'))
r = s.run_ps(ps_script)

print r.status_code
print r.std_out
print r.std_err