import requests
import sys
from bs4 import BeautifulSoup
import hashlib

req = requests.session()
url = sys.argv[1]
r = req.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
payload = dict(hash=hashlib.md5((soup.h3.text).encode()).hexdigest())
flag = req.post(url, data=payload)
print(flag.text)