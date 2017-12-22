import os 
#  os.name
#  系统如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print(os.name)
# print(os.environ)
# print(os.environ.get('Path'))
# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/workspace', 'testdir')
# print(os.path.abspath('testdir'))
# 然后创建一个目录:
# os.mkdir('testdir')
# os.rmdir('testdir')
# a = os.path.split('text.txt')
# print(a)
# os.rename('text.txt','text.py')
# os.remove('text.py')
a = [x for x in os.listdir('.') if os.path.isdir(x)]
print(a)
b = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(b)