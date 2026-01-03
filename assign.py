a, b, _, _ = 1, 2, 3, 4
print(a, b)
c = d = e = 1
print(c, d, e)
d = 2
print(c, d, e)
x = y = [1, [1, '5', 4],2,3]
x[0] = 13
x[1][1] = 2
print(y)