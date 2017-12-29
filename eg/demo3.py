# 例3：
# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，
# 请问该数是多少？
# 审题：
# 求解，在用代码实现计算。
# 程序源代码：
# 方法1：
# 思想：
# 1、设n+100=x^2,n+100+168=y^2
# 2、所n=x^2-100(求n)
# 3、故x^2-y^2=(x+y)(x-y)=168

# list=[]
# for x in range(168):
#     for y in range(x):
#         if x**2 - y**2 == 168:
#             x = y**2 -100
#             list.append(x)
# print("符合条件的有： ",list)
# 方法2： 并集
# 思路：根据公式求x和y的，然后并集操作得结果。
x=map(lambda n:n**2-100,range(1,100))
y=map(lambda n:n**2-100-168,range(1,100))
print(set(list(x))&set(list(y)))
# 这里涉及map函数实用方法。
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，
# 返回包含每次 function 函数返回值的新列表。
