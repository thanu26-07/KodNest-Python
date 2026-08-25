def checker(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
num=int(input())
res=checker(num)
print(res)