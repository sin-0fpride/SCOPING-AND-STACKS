def a():
    x = 10
    print("a: x =", x)
    b()
    print("a after b: x =", x)

def b():
    x = 20
    print("b: x =", x)

x = 5
a()
print("global x =", x)