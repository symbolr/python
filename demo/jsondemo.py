import json
# d = dict(name='Bob', age=20, score=88)
# json.dumps(d)
# print(json.dumps(d))
class Student(object):
 	"""docstring for Student"""
 	def __init__(self, name,age,score):
 		self.name = name
 		self.age = age
 		self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
s = Student('Bob',20,88)
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
print(json.dumps(s,default=student2dict))
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，
# 用来存储实例变量。也有少数例外，比如定义了__slots__的class。
# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)