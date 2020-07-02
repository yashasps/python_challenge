import pickle

fileObject = open("banner.p",'rb')
b = pickle.load(fileObject)


f=""
for y in b:
    for a in y:
        t=str(a[0]*a[1])
        for i in t:
            f += i
    f += "\n"
print(f)