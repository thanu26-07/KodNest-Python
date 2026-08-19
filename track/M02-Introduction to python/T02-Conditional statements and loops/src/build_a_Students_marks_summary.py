n=int(input())
passed=0
failed=0
total=0
for i in range(n):
    mark=int(input())
    if(mark>=40):
        passed+=1
    else:
        failed+=1
    total+=mark
print("Total marks:",total)
print("Passed:",passed)
print("Failed:",failed)
if(failed==0):
    print("Batch result: Passed")
else:
    print("Needs Improvement")