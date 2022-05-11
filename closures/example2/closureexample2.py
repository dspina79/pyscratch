# More Closures

def multiplier(n):
    def multiply(m):
        return m * n
    return multiply

mult1 = multiplier(4)
print(mult1(9))
print(mult1(19))
print(mult1(29))
print(mult1(39))
print(mult1(109))
print(mult1(1009))
