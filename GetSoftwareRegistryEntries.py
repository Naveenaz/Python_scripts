#List softwares installed on the windows system
#Author:Naveen Zunjarwad

import subprocess

import sys

if sys.platform.startswith('win'):
    import _winreg

def get_installed_software():
    """
    Grabs a list of all software that appears in the Uninstall registry keys located at:
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
    HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall
    """
    discovered_keys = []
    discovered_names = []

    path32 = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    path64 = r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    key32 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, path32)
    key64 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, path64)

    # Build list for 32-bit
    for i in range(0, 1000):
        try:
            discovered_keys.append((path32, _winreg.EnumKey(key32, i)))
        except WindowsError:
            break

    # Build list for 64-bit
    for i in range(0, 1000):
        try:
            discovered_keys.append((path64, _winreg.EnumKey(key64, i)))
        except WindowsError:
            break

    # Get clean names if available
    for (path, program) in discovered_keys:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"%s\%s" % (path, program), 0, (_winreg.KEY_ALL_ACCESS + _winreg.KEY_WOW64_64KEY))
        try:
            discovered_names.append(_winreg.QueryValueEx(key, 'DisplayName')[0])
        except:
            discovered_names.append(program)

    #print discovered_names
    return discovered_names

import platform

print platform.python_version()
result= []
result=get_installed_software()

for item in result:
    print item

output = subprocess.Popen("powershell -command \"& {get-wmiobject Win32_Product | select IdentifyingNumber, Name, Version | where {$_.Name -like '*MINT*'} | select IdentifyingNumber, Version}",
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()[0]
print output
