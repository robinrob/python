def outer(some_func):
    def inner():
        return some_func() + 1
    
    return inner

def foo():
    return 1
            
decorated = outer(foo)

print(str(decorated()))