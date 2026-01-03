s = 'Hello, world!'
i = [1,4]
print(s)
print(s[0])
print(s[0:5])
print(s[i[0]:i[1]])

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
a = set('asdjashkajdlfd')
print(a)
a.add('z')
print(a)

b = frozenset('djhfaskjdfnldskha')
print(b)
city = frozenset(["Frank", "Mosc", "Lond"])
print(city)

int_num = 12213
print(type(int_num))
float_num = 10.2
print(type(float_num))
complex_num = 12.3j
print(type(complex_num))
# long_num = 1213313425L # нет long type в python 3
# print(type(long_num))
print('___________')
list = [123, 'abcd', 10.2, 'd']
list1 = ['hello', 'world']
for s in list:
    print(s)
print(list1)
print(list[0:2])
print(list1*2)
print(list + list1)
print('__________')
dic = {'name':'red', 'age':10}
print(dic)
print(dic['name'])
print(dic.values())
print(dic.keys())
print('__________')
tuple = (123,'hello')
tuple1 = ('world',)
print(tuple)
print(tuple[0])
print(tuple + tuple1)
# tuple[1] = 'update' # TypeError: 'tuple' object does not support item assignment
