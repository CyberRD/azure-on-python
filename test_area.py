import winrm

ps_script = """
[int]$intRange = 1200
For ($i=0; $i -le $intRange; $i+=10)
{
    sleep 10
    "Time now: " + $i
}
"""

s = winrm.Session('http://sddseminar9803.cloudapp.net:5985/wsman', auth=('SDD', 'XXX'))
r = s.run_ps(ps_script)

print r.status_code
print r.std_out
print r.std_err