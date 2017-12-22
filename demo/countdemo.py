from collections import Counter
c = Counter()
for ch in 'kalsdljkfa;lsdfja;':
	c[ch] = c[ch]+1
print(c)	