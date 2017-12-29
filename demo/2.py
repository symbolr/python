s1 = 72
s2 = 85
# print('{1:.1f}%'.format(1.11))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', s1))
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for a in L:
	print('Hello,'+a+'!')
