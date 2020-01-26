import sys, requests, json
from config import *

recipient = 'nshoemaker@zero-day.com'

# Site Insights
def get_insights(session):
    url = "https://api.mist.com/api/v1/sites{0}/insights/site{0}/stats?duration=1d&interval=3600&metrics=num_clients,client-dhcp-latency,dns-latency".format(site_id)
    result = session.get(url, headers=headers)

    if result.status_code != 200:
        print('Failed to GET')
        print('URL: {}'.format(url))
        print("Response: {} ({})".format(result.text, result.status_code))

        return []

    result = json.loads(result.text)
    return result

if __name__ == '__main__':
    #Check Variables
    if mist_api_token == '' or site_id == '' or recipient == '':
        print('Missing variables:')
        print('mist_api_token={}'.format(mist_api_token))
        print('site_id={}'.format(site_id))
        print('recipient={}'.format(recipient))

    sys.exit(1)

# Session Creation
session = requests.Session()

# Call Insights Function
insights = get_insights(session)

num_results = len(insights.get('rt', []))

idx = 0
body = 'Org ID: ' + org_id + '\n'
body += 'Site ID: ' + site_id + '\n'

while idx < num_results:
    num_clients = int(insights['num_clients'][idx] or 0)
    dhcp_latency = round((insights['client-dhcp-latency'][idx] or 0), 5)
    dns_latency = round((insights['dns-latency'][idx] or 0), 5)

    body += '\n{0}\tclients={1:03d}\tdhcp_latency={2:f}\tdns_latency={3:f}'.format(insights['rt'][idx], num_clients, dhcp_latency, dns_latency)
    idx += 1

try:
    body += '\n\n=====\n\n'

except Exception as e:
    print(e)
    print('Exiting Script.')
    sys.exit(2)

print(body)

send_email(recipient, 'Email Report for Site Insights', body)
