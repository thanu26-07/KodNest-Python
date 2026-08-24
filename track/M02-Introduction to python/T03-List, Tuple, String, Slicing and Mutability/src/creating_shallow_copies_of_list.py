skills=[]
for _ in range(5):
    skills.append(input())
tup=tuple(skills)
print(tup)
print("first two",tup[:2])
print("Last two",tup[-2:])
print("alternate",tup[::2])
print("Reversed",tup[::-1])