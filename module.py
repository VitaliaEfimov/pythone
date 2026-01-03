import helloWorld as hw
from helloWorld import sayHello

print(hw.__doc__)

print(hw.sayHello.__doc__)
print(__name__)

if __name__ == '__main__':
    print(1)
    sayHello()