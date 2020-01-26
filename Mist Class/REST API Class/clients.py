import sys, requests, json
from config import *

# =======
# Functions
# =======

# WiFi Client Stats
def get_client_stats(session):
    url = 'https://api.mist.com/api/v1/sites/{}/stats/clients'.format(site_id)

    result = session.get(url, headers=headers)

    if result.status_code != 200:
        print('Failed to GET')
        print('URL: {}'.format(url))
        print('Response: {} ({})'.format(result.text, result.status_code))

        return []

    result = json.loads(result.text)

    return result

# =======
# Main
# =======

# Ensure variables
if mist_api_token == '' or site_id == '':
    print('Missing variables:')
    print('mist_api_token={}'.format(mist_api_token))
    print('site_id={}'.format(site_id))

    sys.exit(1)


# Session Setup
session = requests.Session()

# WiFi Client Function Call
clients = get_client_stats(session)

# Build client dictionary
client_dict = {}

for client in clients:
    if 'ap_mac' not in client:
        continue

    ap = client['ap_mac']

    if ap in client_dict:
        client_dict[ap].append(client)
    else:
        client_dict[ap] = [client]

print()
for key in client_dict:
    print('{} client(s) on AP {}'.format(len(client_dict[key]), key))

    for client in client_dict[key]:
        print('{:>30} ({})\tband={:<2}  channel={:<3}  proto={}'.format(client['username'] if client.get('username', None) else client.get('hostname', 'Unknown'),
        client['mac'],
        client['band'],
        client['channel'],
        client['proto']
        ))

print()
