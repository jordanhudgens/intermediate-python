# Install using python3.4 -m pip install requests

import requests

r = requests.get('https://api.github.com/events')

# print(r)
# print(r.text)
# print(r.content)
print(r.json())