#!/usr/bin/python
#
# main.py
#
# Contains the Mist API configuration variables used for the API class and prints to the terminal.

# =====
# VARIABLES
# =====

# This is the Mist API token that must be included with each Mist API call.
# This token is returned when logging into the Mist API using the following credentials...
#    Username = livedemo@mistsys.com
#    Password = password_goes_here
#
# See the Mist API documentation for more detailed info:
#    https://api.mist.com/api/v1/docs/Auth#api-token
mist_api_token = 'EBojC8yjv7OdDbURSWZ5nTc6qIA3M856t8WncERxnTiHHW9nVxl4gyX2lncWgPr0JINGHIsIavxdVMUUb4OhAkHYeiuhoMH7'

# This is the Mist "Organization ID" for the class.
org_id = '3896a314-69a7-4ecb-b1ca-b9e9a99c3549'  # Live Demo

# This is the Mist "Site ID" for the class. Each Mist "organization" contains multiple "sites".
site_id = 'afbdf51c-a089-4a27-8197-afe851a1ddcf'  # Live Demo

# This is the Mist "Map ID" for the class. Each Mist "site" contains multiple "maps".
#map_id = '21f849d4-d12f-4feb-b40f-5be0e2aef8cf' # Live Demo Office

# This is the set of HTTP headers used for each Mist API call.
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + mist_api_token
}

# =====
# MAIN
# =====

# Print each of the Mist API configuration settings.
print('Mist API Token: {}'.format(mist_api_token))
print('Mist Org ID: {}'.format(org_id))
print('Mist Site ID: {}'.format(site_id))
#print('Mist Map ID: {}'.format(map_id))
print('Mist API Headers:')
for key, val in headers.items():
    print('   {} = {}'.format(key, val))
