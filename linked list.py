import urllib.request
from string import *
url='http://www.pythonchallenge.com/pc/def/equality.html'

with urllib.request.urlopen(url) as url:
    s = url.read()

mess = list(s.decode().split("<!--")[1].replace("-->","").replace("\n",""))

for i in range(0,len(mess)):
    if mess[i] in ascii_lowercase and mess[i-1] in ascii_uppercase and mess[i-2] in ascii_uppercase and mess[i-3] in ascii_uppercase and mess[i+1] in ascii_uppercase and mess[i+2] in ascii_uppercase and mess[i+3] in ascii_uppercase and mess[i-4] in ascii_lowercase and mess[i+4] in ascii_lowercase:
        print(mess[i])

