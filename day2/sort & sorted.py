list1 = "This is a test string".split()


def change_lower(str_name: str):
    return str_name.lower()


print(sorted(list1, key=change_lower))  # key可以传递比较规则的函数，
# 这里使用change_lower函数将字符串全部转换为小写后排序

list1.sort(key=change_lower)  # sort()方法也可以使用key参数
print(list1)

print('-' * 50)
str_tuples = [('apple', 2), ('banana', 1), ('orange', 3)]
print(sorted(str_tuples, key=lambda x: x[1]))  # lambda函数是用来定义一个匿名函数的，
# 这里使用lambda函数将元组的第二个元素作为排序的依据

print('-' * 50)
from operator import itemgetter, attrgetter

print(sorted(str_tuples, key=itemgetter(1)))  # 使用itemgetter函数可以直接获取元组的第二个元素作为排序的依据
print('-' * 50)
print(sorted(str_tuples, key=itemgetter(0, 1)))  # 还可以传入多个参数，表示多个元素作为排序的依据
print('等价于', sorted(str_tuples, key=lambda x: (x[0], x[1])))
print('-' * 50)
my_dict = {'Li': ['M', 7],
           'Wang': ['K', 8],
           'Zhang': ['J', 9],
           'Chen': ['O', 6]}
print(sorted(my_dict.items(), key=lambda x:x[1][1]))
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         """
#         相对于__str__方法，__repr__方法返回非字符串的形式
#         :return:
#         """
#         return repr((self.name, self.age))  # 返回元组的形式
#
#
# student1 = Student('Alice', 20)
# print(student1)
