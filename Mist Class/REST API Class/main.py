# API configuration variables

# =======
# Variables
# =======

mist_api_token = 'EBojC8yjv7OdDbURSWZ5nTc6qIA3M856t8WncERxnTiHHW9nVxl4gyX2lncWgPr0JINGHIsIavxdVMUUb4OhAkHYeiuhoMH7'

org_id = '3896a314-69a7-4ecb-b1ca-b9e9a99c3549'

site_id = 'afbdf51c-a089-4a27-8197-afe851a1ddc'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + mist_api_token
}

# =======
# Main
# =======

# Prints out each of the API configutation settings
print('Mist API Token: {}'.format(mist_api_token))
print('Mist Org ID: {}'.format(org_id))
print('Mist Site ID: {}'.format(site_id))
print('Mist API Headers:')
for key, val in headers.items():
    print('   {} = {}'.format(key, val))
