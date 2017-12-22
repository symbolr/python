from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())

h = StringIO('hello\nHi\nGoodBye')
while  True:
	 s = h.readline()
	 if s=='':
	 	break
	 print(s.strip())	