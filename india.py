import requests
import base64
import soundfile
#import numpy

url="http://www.pythonchallenge.com/pc/hex/bin.html"

s=requests.get(url,auth=("butter","fly"))
s=s.text
r=s.split("base64\n\n")[1].split("\n\n--===============1295515792==--")[0]
f=base64.b64decode(r)

india=open("indaisn.wav",'wb')
india.write(f)
india.close()
india=open("indaisn.wav",'rb')
x=soundfile.SoundFile('indaisn.wav')

#indi = open("iendian.wav", "wb")
soundfile.write('iendian.wav',
                data=x.read(),
                samplerate=x.samplerate,
                subtype=x.subtype,
                endian='FILE',
                format=x.format)




