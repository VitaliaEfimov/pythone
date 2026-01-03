names = ['kile', 'stan', 'keine', 'eric']
print(names)
for i in range(-4, 4):
    print(f'num {i} name {names[i]}')
print(names.append('wendy'))
print(names)
print(names.insert(0, 'token'))
print(names)
print(names.remove('keine'))
print(names)
print(names.index('eric'))
print('-----------------')
a = [1, 1, 1, 2, 3, 4]
print(a.count(1))
print(a.count(2))
print(a.count(3))
print(a.count(4))
print('------------')
a.reverse()
print(a)
print(a[::-1])
for i in range(len(a)):
    print(a.pop())
print(a)
for n in names:
    print(n)