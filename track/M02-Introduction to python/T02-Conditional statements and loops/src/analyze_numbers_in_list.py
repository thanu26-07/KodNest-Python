limit=int(input())
target=int(input())
count=0
total=0
found=False
for i in range(1,limit+1):
    if (i%3==0):
        count+=1
        total+=i
        if(target==i):
            found=True
print(count)
print(total)
print(found)
