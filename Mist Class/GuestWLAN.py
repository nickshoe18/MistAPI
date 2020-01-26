import sys
import requests
import json

from mist_client import Admin

mist_api_token = 'EBojC8yjv7OdDbURSWZ5nTc6qIA3M856t8WncERxnTiHHW9nVxl4gyX2lncWgPr0JINGHIsIavxdVMUUb4OhAkHYeiuhoMH7'
org_id = '3896a314-69a7-4ecb-b1ca-b9e9a99c3549'

if _name_ == '_main_':
    admin = Admin(mist_api_token)

    payload = {
        "ssid": "Batcave Guest",
        "enabled": True,
        "auth": {
            "type": "psk",
            "psk": "Iamnotbrucewayne",
        },
    }

api_url = 'https://api.mist.com/api/v1/sites/{}/wlans'.format(org_id)
result = admin.post(api_url, payload)

print('\nWLAN = {}\n'.format(result))
