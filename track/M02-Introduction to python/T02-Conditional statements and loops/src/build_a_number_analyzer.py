n=int(input())
pos=0
neg=0
zero=0
total=0
for i in range(n):
    num=int(input())
    if(num==0):
        zero+=1
    elif(num>0):
        pos+=1
    else:
        neg+=1
    total+=num
print(total)
print(pos)
print(neg)
print(zero)