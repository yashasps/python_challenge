numbers="1"
def counting(numbers):
    count = 0
    lastterm = numbers[0]
    x = ""
    for i in numbers:
        if i is lastterm:
            count+=1
        else:
            x += str(count) + lastterm
            count=1
        lastterm=i

    x+=str(count)+lastterm
    return(x)
for i in range(0,30):
    numbers=counting(numbers)

print(len(numbers))