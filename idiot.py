import requests

url="http://www.pythonchallenge.com/pc/hex/unreal.jpg"

header={'Content-Type': 'image/jpeg', 'Content-Range': 'bytes 0-30202/2123456789', 'Transfer-Encoding': 'chunked', 'Date': 'Sat, 20 Apr 2019 17:40:29 GMT', 'Server': 'lighttpd/1.4.35'}

#while True:
end=2123456789
response=requests.get(url,auth=("butter","fly"),headers=header)
bytes=response.headers['Content-Range']

bytes=int(bytes.split("-")[1].split("/")[0])+1

header['Range']='bytes=%i-%i'  %(1152983631,end)
#response=requests.get(url,auth=("butter","fly"),headers=header)
y=response.content
print(response.headers['Content-Range'])

new=open("more.zip",'wb')
new.write(y)



g=""
f="esrever ni emankcin wen ruoy si drowssap eht"
print(f[::-1])

