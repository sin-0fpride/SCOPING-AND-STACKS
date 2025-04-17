# Define a function f that takes a parameter x
def f(x):
    # Define a nested function g (closure)
    def g():
        # Local variable x in g, shadows the x in f
        x = 'abc'
        print('x =', x)  # prints local x of g: 'abc'

        # Define another nested function h inside g
        def h():
            # z is assigned the value of x from g's scope (which is 'abc')
            z = x
            print('z =', z)  # prints 'z = abc'

        x = x + '1'  # Concatenates '1' to 'abc', x becomes 'abc1'
        print('x =', x)  # prints updated x: 'abc1'
        h()  # Calls function h
        g()  # Calls g again (recursive call, but might be problematic - we'll check)
        print('x =', x)  # Prints again: 'abc1'
        return g  # Returns the function g

# Outside the function now:
x = 3  # Global variable x
z = f(x)  # Call f(3), which returns g and assigns it to z
print('x =', x)  # Prints global x: 3
print('z =', z)  # z now holds the function g (returned by f)
z()  # Calls the returned function g (with its inner behavior)