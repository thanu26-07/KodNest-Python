n=int(input())
scores=[]
total=0
for i in range(n):
    num=int(input())
    scores.append(num)
    total+=num
search_score=int(input())
highest=max(scores)
lowest=min(scores)
print(highest)
print(lowest)
if search_score in scores:
    print("Found")
else:
    print("Not Found")
