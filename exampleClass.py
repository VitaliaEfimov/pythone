class ExampeClass:
    def __init__(self):
        self.name = 'example'
    
    def someFunction(self, a):
        if a > 5:
            return True
        else:
            return False
        
def separateFunction(b):
    for i in b:
        if i == 1:
            return True
    return False

print(separateFunction([1,2,3,4,5,6]))
print(separateFunction([6,6]))
example = ExampeClass()
print(example.name)
print(example.someFunction(2))
print(example.someFunction(6))