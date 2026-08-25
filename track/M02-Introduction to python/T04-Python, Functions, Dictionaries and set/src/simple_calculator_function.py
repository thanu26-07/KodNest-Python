def calculate(first, second, operator):
    if operator=='+':
        return first+second
    elif operator=='-':
        return first-second
    elif operator =='*':
        return first*second
    else:
        return first/second
first=int(input())
second=int(input())
operator=input()
res=calculate(first,second, operator)
print(res)