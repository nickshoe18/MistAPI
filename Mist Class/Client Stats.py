import os,sys,subprocess,json

token = "bD4syoPW3PJEQx6zznt3ao3xVa8vkPqgS090AtkDPOFauP0hhUexPw3iwmKq1he7nwL3cGug4quPlfanoc1WVwEocW42KSzs"
curlget = 'curl -H "Authorization: Token {}" "https://api.mist.com/api/v1/'.format(token)
siteid = "afbdf51c-a089-4a27-8197-afe851a1ddcf"

cmd = curlget + 'sites/{}/stats/clients"'.format(siteid)
results = subprocess.check_output(cmd,shell=True)
clients = json.loads(results)
client_protocols_count = {}
for c in clients:
    if c["proto"] not in client_protocols_count:
        client_protocols_count[c["proto"]] = 1
    else:
        client_protocols_count[c["proto"]] += 1

for k,v in client_protocols_count.dictitems():
    print(k,":",v)
