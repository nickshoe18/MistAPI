import requests
import json

url = 'https://api.mist.com/api/v1/orgs/3896a314-69a7-4ecb-b1ca-b9e9a99c3549/wlans'

headers = {
    'Content Type': "application/json",
    'Authorization': 'Token EBojC8yjv7OdDbURSWZ5nTc6qIA3M856t8WncERxnTiHHW9nVxl4gyX2lncWgPr0JINGHIsIavxdVMUUb4OhAkHYeiuhoMH7'
}

results = requests.get(url, headers=headers)
wlans = json.loads(results.text)

for wlan in wlans:
    print(wlan['ssid'], ">", wlan["id"])
