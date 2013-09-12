import unittest

from robarray import Array

class TestCase(unittest.TestCase):
    
    def test_should_set_and_get_element(self):
        arr = Array(1)
        
        arr[0] = 0
        
        self.assertEquals(0, arr[0])
        
    
    def test_should_clear_values_using_0(self):
        arr = Array(1)
        
        arr.clear(0)
        
        self.assertEquals(0, arr[0])
        
        
    def test_should_return_correct_length(self):
        arr = Array(5)
        
        arr.clear(0)
        
        self.assertEquals(5, len(arr))
        
        
    def test_should_be_iterable(self):
        arr = Array(5, value=0)

        for element in arr:
            element = 1
        
        self.assertEquals(1, arr[0])
        
        
if __name__ == '__main__':
    unittest.main()