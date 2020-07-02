import zlib
import bz2

previous=open("more", errors='ignore')
data=previous.read()

h=zlib.decompress(data)
print(h)