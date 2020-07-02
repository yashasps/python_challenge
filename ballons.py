
import difflib
file=open("deltas.gz",'rb')
lines=file.readlines()
for line in lines:
    print(['{:02X}'.format(b) for b in line])

differ=difflib.differ()
differ.compare(a,b)