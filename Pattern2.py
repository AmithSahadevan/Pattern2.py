Input = input("Enter a phrase: ").upper()
lzt = list(Input)

k = len(lzt)+1

for i in range(k):
	k = k - 1
	for j in range(k):
		print(lzt[j], end = "")
	print()