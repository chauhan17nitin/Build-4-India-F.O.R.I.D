import os
import time
import subprocess

class Connect():
    def __init__(self):
        self.wpa_supplicant_conf = "/etc/wpa_supplicant/wpa_supplicant.conf"
        self.sudo_mode = "sudo "

    def wifi_connect(self, ssid, psk):
        print(ssid,psk)
        cmd_result = ""

        # write wifi config to file
        f = open('wifi.conf', 'w')
        f.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n')
        f.write('update_config=1\n')
        f.write('country=US\n')
        f.write('\n')
        f.write('network={\n')
        f.write('    ssid="' + ssid + '"\n')
        f.write('    psk="' + psk + '"\n')
        f.write('    key_mgmt=WPA-PSK\n')
        f.write('}\n')
        f.close()
        time.sleep(1)

        # move to the specific folder and overwrite the old file
        cmd = 'sudo mv wifi.conf ' + self.wpa_supplicant_conf
        cmd_result = os.system(cmd)
        print(cmd + " - " + str(cmd_result))
        time.sleep(1)

        # reconfigure the wifi service
        cmd = 'wpa_cli -i wlan0 reconfigure'
        cmd_result = os.system(cmd)
        print(cmd + " - " + str(cmd_result))
        time.sleep(10)

        # keep all the information about the network
        p = subprocess.Popen(['ifconfig', 'wlan0'], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        out, err = p.communicate()
        ip_address = "<Not Set>"

        # extract the IP address
        for l in out.split(b'\n'):
            if l.strip().startswith(b'inet '):
                ip_address = l.strip().split(b'inet ')[1].split(b' ')[0]

        return ip_address


