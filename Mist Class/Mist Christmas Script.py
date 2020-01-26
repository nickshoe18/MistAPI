import os,sys,subprocess,time

token = 'EBojC8yjv7OdDbURSWZ5nTc6qIA3M856t8WncERxnTiHHW9nVxl4gyX2lncWgPr0JINGHIsIavxdVMUUb4OhAkHYeiuhoMH7'
curlpost = 'curl -X POST -H "Authorization: Token {}" "https://api.mist.com/api/v1/'.format(token)
siteid = "afbdf51c-a089-4a27-8197-afe851a1ddcf"

for ap in ["5c5b350e174d"]:
    cmd = curlpost + 'sites/{}/devices/00000000-0000-0000-1000-{}/locate"'.format(siteid,ap)
    subprocess.check_output(cmd,shell=True)
    time.sleep(3)
    cmd = curlpost + 'sites/{}/devices/00000000-0000-0000-1000-{}/unlocate"'.format(siteid,ap)
    subprocess.check_output(cmd,shell=True)
