def make_pretty(func):
    def inner():
        print("This is the inner function")
        func()
    return inner

def orignal():
    print("Orignal function")
    
pretty=make_pretty(orignal)

#Output: <function make_pretty.<locals>.inner at 0x0000022D0F632040>
pretty

pretty()

@make_pretty
def test():
    print("Test")

test()