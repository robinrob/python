import unittest

from robarray import Array

class TestCase(unittest.TestCase):
    
    def test_should_set_and_get_element(self):
        arr = Array(1)
        
        arr[0] = 0
        
        self.assertEquals(0, arr[0])


    def test_should_return_correct_length(self):
        arr = Array(5)

        self.assertEquals(5, len(arr))
        
    
    def test_should_clear_values_with_99(self):
        arr = Array(1)
        value = 99
        
        arr.clear(value)

        for i in range(len(arr)):
            self.assertEquals(value, arr[i])

        
    def test_should_iterate_over_all_elements(self):
        arr = Array(5, value=0)

        cunt = 0
        for element in arr:
            cunt += 1

        self.assertEquals(len(arr), cunt)
        
        
if __name__ == '__main__':
    unittest.main()