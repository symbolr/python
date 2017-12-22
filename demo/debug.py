# 第一种打print
# def foo(s):
# 	n = int(s)
# 	print('>>>n = %d' %n)
# 	return 10/n

# def main():
# 	foo('0')

# main()		

# 第二种断言
# def foo(s):
# 	n = int(s)
# 	assert n!= 0 ,'n is zero'
# 	return 10/n

# def main():
# 	foo('0')

# main()

# 第三种 logging 
#
# logging.basicConfig(level=logging.INFO)
# def foo(s):
# 	n = int(s)
# 	logging.info('>>>n = %d' %n)
# 	return 10/n

# def main():
# 	foo('0')

# main()

# 第四种 pdb 
# def foo(s):
# 	n = int(s)
# 	return 10/n

# def main():
# 	foo('0')

# main()
import pdb  
def foo(s):
	n = int(s)
	pdb.set_trace()
	return 10/n

def main():
	foo('0')

main()