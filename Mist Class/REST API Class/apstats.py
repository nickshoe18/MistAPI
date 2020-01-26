import sys, requests, json
from config import *

# =======
# Functions
# =======

#AP Stats Function
def get_device_stats(session):
    url = 'https://api.mist.com/api/v1/sites/{}/stats/devices'.format(site_id)

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

# Make sure variables are defined properly
if mist_api_token == '' or site_id == '':
    print('Missing variables:')
    print('mist_api_token={}'.format(mist_api_token))
    print('site_id={}'.format(site_id))

    sys.exit(1)

# Create session to dashboard
session = requests.Session()

# Function to get AP stats
devices = get_device_stats(session)

# AP dictionary by MAC Address
device_dict = {}

for device in devices:
    if 'mac' not in device:
        continue

    ap = device['mac']

    if ap in device_dict:
        device_dict[ap].append(device)
    else:
        device_dict[ap] = [device]

print()
for key in device_dict:
    for d in device_dict[key]:
        # AP stats
        print('AP "{}"'.format(key))
        print('================')
        print('     Status = "{}"'.format(d.get('status', '').upper()))
        print('     IP Address = "{}"'.format(d.get('ip', '')))
        print('     Serial Number = "{}"'.format(d.get('serial', '')))
        print('     Uptime (secs) = {}'.format(d.get('uptime', '')))
        print('     Number of clients = {}'.format(d.get('num_clients', '')))
        print('     WiFi total tx bytes = {}'.format(d.get('tx_bytes', '')))
        print('     WiFi total rx bytes = {}'.format(d.get('rx_bytes', '')))

        # 5GHz radio stats
        radios = d.get('radio_stat', [])
        if 'band_5' in radios:
            print('   Radio 5 GHz:')
            for key, val in radios['band_5'].items():
                print('       {} = {}'.format(key, val))

        # 2.4GHz radio stats
        if 'band_24' in radios:
            print('     Radios 2.4 GHz:')
            for key, val in radios['band_24'].items():
                print('        {} = {}'.format(key,val))

        # BLE stats
        if 'ble_stat' in d:
            ble = d['ble_stat']
            print('    BLE:')
            print('        tx packets = {}'.format(ble.get('tx_pkts', '')))
            print('        rx packets = {}'.format(ble.get('rx_pkts', '')))
        print()
