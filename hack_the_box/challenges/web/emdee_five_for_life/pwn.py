import requests
import sys
from bs4 import BeautifulSoup
import hashlib

# Script to grab html from website, extract string and then MD5hash
# Then post back to website to retrieve flag in response text
# Script usage: python3 pwn.py <url_of_challenge_site>

# Create a session to use with requests
req = requests.session()
url = sys.argv[1]
r = req.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
payload = dict(hash=hashlib.md5((soup.h3.text).encode()).hexdigest())
flag = req.post(url, data=payload)
print(flag.text)
