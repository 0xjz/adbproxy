#!/usr/bin/env python
import subprocess
import os
import sys

def get_ip(interface='en0'):
    s = subprocess.check_output(['ifconfig', interface])
    return s.split('inet ')[1].split(' ')[0]

def set_proxy(ip, port=8080):
    os.system('adb shell settings put global http_proxy %s:%d' % (ip, port))

if __name__ == '__main__':
    interface = 'en0'
    port = 8080
    if len(sys.argv) >= 2:
        interface = sys.argv[1]
    elif len(sys.argv) >= 3:
        port = int(sys.argv[2], 10)
    print('interface   --> "%s"' % interface)
    ipaddr = get_ip(interface)
    print('ip addr     --> "%s"' % ipaddr)
    print('proxy port  --> "%d"' % port)
    set_proxy(ipaddr, port)
    print('done.')

