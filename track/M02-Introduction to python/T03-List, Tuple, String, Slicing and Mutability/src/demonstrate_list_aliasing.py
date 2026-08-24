original_scores=[]
for _ in range(3):
    original_scores.append(int(input()))
alias_scores=original_scores
replace=int(input())
additional=int(input())
alias_scores[0]=replace
alias_scores.append(additional)
print(original_scores)
print(alias_scores)
print("Shared Object:")
print(original_scores is alias_scores)