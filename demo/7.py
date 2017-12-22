# L=[]
# n=1
# while n<100:
# 	L.append(n)
# 	n=n+2

# for x in L:
# 		print(x)	
def trim(s):
    if (s == ''):
        pass
    elif (s[0] == ' '):
        s = trim(s[1:])
    elif (s[-1] == ' '):
        s = trim(s[0:-1])
    return s
a = trim('    asfasdfa   ') 
print a  