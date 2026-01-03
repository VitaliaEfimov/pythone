a = [12, 'b', True, (1,2), None]
for i in a:
    if isinstance(i, int):
        print(f'Integer {i}')
    else :
        if isinstance(i, str):
            print(f'String {i}')
        else : 
            if i is None: print(None)
            print(f'Unknow type {type(i)}')

b = '123.456'
print(float(b))
print(int(float(b)))
# print(int(b))

s = 'Hello'
print(list(s))
print(set(s))
print(tuple(s))
print(u'Привет')
print('foo\nbar')
print('foo\\nbar')
print(r'foo\\nbar')

def f(m):
    m.append(3)
x = [1,2]
f(x)
print(x)