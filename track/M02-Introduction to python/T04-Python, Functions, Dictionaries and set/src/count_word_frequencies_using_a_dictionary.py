n=int(input())
word_fre={}
for _ in range(n):
    word=input().strip()
    word_fre[word]=word_fre.get(word,0)+1
for word, count in word_fre.items():
    print(word, count, sep=" ")