words = input().split()
keyword = input()

for i in range(len(words)):
	for j in range(len(keyword)):
		if keyword[j] in words[i]:
			print (words[i], end=' ')
			break

print ()
