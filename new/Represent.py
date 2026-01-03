class Represent(object):
    def __init__(self, x, y):
        self.x, self.y = x,y

    def __repr__(self):
        return "Represent(x={},y={})".format(self.x, self.y)
    
    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)

r = Represent(1, "Hopper")
print(r)
print(r.__repr__)
rep = r.__repr__
print(rep)
print(type(rep))
r2 = eval(rep)
print(r2)
print(r2 == r)