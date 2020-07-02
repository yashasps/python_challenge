import datetime
import calendar
import urllib.request

with urllib.request.urlopen(url) as url:
    s = url.read()

for i in range(1006,1996,10):
    today = datetime.datetime(i,1,26)
    if today.weekday()==0:
        if calendar.isleap(i):
            print(i)


