import unittest
from learn import MyClass

class TestMyClass(unittest.TestCase):
    def test_expensive_computation(self):
        obj = MyClass(10)
        self.assertEqual(obj.expensive_computation, 20)

if __name__ == '__main__':
    unittest.main()