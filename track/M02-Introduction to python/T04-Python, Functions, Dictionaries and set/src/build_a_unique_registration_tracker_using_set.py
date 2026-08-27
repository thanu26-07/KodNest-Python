n=int(input())
registrations=set()
for _ in range(n):
    st_id=input().strip()
    registrations.add(st_id)
search=input().strip()
unique=len(registrations)
duplicate=n-unique
print("Unique count",unique)
print("Duplicate count",duplicate)
if search in registrations:
    print("Registration found")
else:
    print("Registration not found")