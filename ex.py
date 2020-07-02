w,h=7,99
k=0
j=0
n=0
while w!=3:
    for j in range(0,w//2):

        for i in range(k, w):
            print(n)
            if w-i<=n:
                n = w - i
                break
            else:
                print("                "+str(w-i))
        k += 1
    n=w-i



    w-=1
    h-=1
    if j>0:
        k+=1
        j+=1