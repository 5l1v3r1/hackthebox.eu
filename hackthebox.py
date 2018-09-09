#!/usr/bin/env python3
import requests, base64, sys

def hackthebox(num):
   print('Your invite code(s):')
   
   for i in range(int(num)):
    # Post request to the API
    c = requests.post('https://www.hackthebox.eu/api/invite/generate')
	
	# print decoded code from base64 and UTF-8
    print('%i) %s' % (int(i), base64.b64decode(c.json()['data']['code']).decode('utf-8')))

# Print Invite code
hackthebox(sys.argv[1])
