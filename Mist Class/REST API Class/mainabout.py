# =========
# Imports
# =========
import requests, json

# ==========
# Variables
# ==========

# Set HTTP headers
headers = {'Content-Type': 'application/json'}

# ===========
# Main
# ===========
session = requests.Session()

url = 'https://api.mist.com/api/v1/about'

result = session.get(url, headers=headers)

result = json.loads(result.text)

print("\nAbout Response...")
for key, val in result.items():
    print("   {} = {}".format(key, val))
print()
