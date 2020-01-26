import sys, requests, json

# =====
# Variables
# =====

mist_api_token = 'EBojC8yjv7OdDbURSWZ5nTc6qIA3M856t8WncERxnTiHHW9nVxl4gyX2lncWgPr0JINGHIsIavxdVMUUb4OhAkHYeiuhoMH7'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token ' + mist_api_token
}

# ======
# Main
# ======

# Make sure variables are defined
if mist_api_token == '':
    print('Missing Variable:')
    print('mist_api_token={}'.format(mist_api_token))

    sys.exit(1)

session = requests.Session()

url = 'https://api.mist.com/api/v1/self'

# Request for 'Self' information
result = session.get(url, headers=headers)

# Verify request was successful
if result.status_code != 200:
    print('Failed to GET')
    print('URL: {}'.format(url))
    print('Response: {} ({})'.format(result.text, result.status_code))

    sys.exit(1)

# Convert response to json
result = json.loads(result.text)

# Display Self info
print('\nSelf Response...')
for key, val in result.items():
    print('   {}={}'.format(key, val))
print()
