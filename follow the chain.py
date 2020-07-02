import urllib.request
from string import *

url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

def search(url):
    with urllib.request.urlopen(url) as url:
        s = url.read()
    s=str(s)
    url1=repe(s)
    for x in range(0,440):
        with urllib.request.urlopen(url1) as url1:
            s = url1.read()
        s = str(s)
        url1=repe(s)
        print(url1)

def repe(s):
    p = ""
    for i in s:
        if i in ascii_lowercase or i is "'" or i is " ":
            continue
        else:
            p += i
    url1 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(p)
    return url1

search(url)

