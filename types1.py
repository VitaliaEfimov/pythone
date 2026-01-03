b1 = True
b2 = False
if (b1 == 1): print("TRUE = 1")
if (b2 == 1): print("FALSE = 0")
print(f'TRUE AND FALSE {b1 and b2}')
print(f'TRUE AND FALSE {b1 or b2}')
print(f'NOT TRUE {not b1}')
print(f'NOT FALSE {not b2}')
x = 123234e100
print(type(x))
print(x)
c = 10 + 34 + 2j
print(type(c))
print(c)
s = 'Hello'
print(type(s))
print(s)
by = b'Hello'
print(type(by))
print(by)
for b in by:
    print(type(b))
    print(b)
a = reversed("Hello")
print(type(a))
for ab in a:
    print(type(ab))
    print(ab)

con = (1, 3, 2, 'a', (1,2), [1,2])
print(type(con))
print(con)
se = {1, 3, 2, 'a'}
print(type(se))
print(se)
ma = {1: 'a', 2: 'b'}
print(type(ma))
print(ma)
for i in ma.keys():
    print(f'key {i}, set {ma[i]}')