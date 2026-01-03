def sayMooo():
    print('Mooooo!')

s = """w'o'w"""
print(s)
print(repr(s))
print(str(s))
print(eval(repr(s)) == s)
# print(eval(str(s)) == s)

import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today))