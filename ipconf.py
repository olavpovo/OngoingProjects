import subprocess
from os import system

def set_dns():
    wlan="ipconfig getifaddr en0"

    def get_ip(wlan):
        ip_address= subprocess.check_output(wlan,shell=True,text=True)
        ip_address=ip_address.replace("\n","")
        print(f"IP Address is {ip_address}")
        return ip_address
    
    ip=get_ip(wlan)

    if ip == "192.168.1.100":
        system(f"networksetup -setdnsservers Wi-Fi empty")
    else:
        print(f"DNS Server set to {ip}")
        system(f"networksetup -setdnsservers Wi-Fi {ip}")

set_dns()