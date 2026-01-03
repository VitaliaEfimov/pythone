from collections import defaultdict

tu1 = ('example',)
tu2 = 'example',
tu3 = (['example'])
print(len(tu1))
print(len(tu2))
print(len(tu3))
print(type(tu1))
print(type(tu2))
print(type(tu3))

dic = {1 : 'One', 2 : 'Two', 3 : 'Three'}
print(dic[1])

for n in dic.keys():
    print(f'{n} это {dic[n]}')

first_names = {'Adam', 'Bob', 'Cyle'}

my_list = [1,2,3]
print(type(set(my_list)))

for name in first_names:
    print(name)

#print(dic[4]) ошибка Traceback (most recent call last):
#  File "/Users/vitalaefimov/python/tu.py", line 25, in <module>
#    print(dic[4])
#KeyError: 4
print('--------------------')

defdic = defaultdict(lambda: 'Not found')
defdic['one'] = 'Adam'
defdic['two'] = 'Bob'
defdic['three'] = 'Cyle'
defdic[1] = 'Dyny'
print(defdic['not'])
print(defdic['one'])
print(defdic['two'])
print(defdic['three'])
print(defdic[1])
