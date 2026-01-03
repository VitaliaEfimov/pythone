import unittest

class TestMathFunctions(unittest.TestCase):
    
    def test_addition(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
        # print('success add test!')
        
    def test_subtraction(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)
        # print('success subtract test!')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    unittest.main()