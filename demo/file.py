f = open('text.txt', 'w')
# print(f.read())
f.write('wowowoowowowowow')
f = open('text.txt', 'r')
for line in f.readlines():
	print(line.strip())
# jpg = open('test.jpg', 'rb')
# print(jpg.read())
# 
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
