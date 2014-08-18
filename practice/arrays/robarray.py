from ctypes import py_object

from errors import ArrayInitialisationException

class RobArray:

    def __init__(self, size, value=0):
        if (size <= 0):
            raise ArrayInitialisationException()
        else:            
            self.elements = (py_object * size)()
            self.clear(value)
            
    
    def __len__(self):
        return len(self.elements)
    
    
    def __getitem__(self, index):
        return self.elements[index]
    
    
    def __setitem__(self, index, value):
        self.elements[index] = value
        return self.elements
    
    
    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value
            
            
    def __iter__(self):
        self.next = -1
        return self
    
    
    def __next__(self):
        if self.next < len(self) - 1:
            self.next += 1
            return self.elements[self.next]
        else:
            raise StopIteration
    
    
    def __str__(self):
        s = "[ "
        
        for element in self:
            s += str(element) + " "

        s += "]"
        
        return s