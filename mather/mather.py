class Mather:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        try:
            return x / y
        except ValueError:
            print("Value error found")
            return 0
        except:
            print("Some other error")
            return 0
    
    @staticmethod
    def get_hypotenuse(a, b):
        return float(((a * a) + (b * b))) ** (1/2)

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            x = n - 1
            while x > 1:
                if n % x == 0:
                    return False
                x -= 1
        return True

    @staticmethod
    def worst_power(base, exp):
        if exp < 0:
            raise RuntimeError
        val = 1
        for i in range(0, exp):
            val *= base
        
        return val

x = 10
y = 15
z = 0

print(Mather.add(x, y))
print(Mather.subtract(x, y))
print(Mather.multiply(x, y))
print(Mather.divide(x, y))

a = 3
b = 4
c = Mather.get_hypotenuse(a, b)
print("The hypotenuse is", c)

a = 6
b = 8
c = Mather.get_hypotenuse(a, b)
print("The hypotenuse is", c)

base = 2
exp = 4
print(Mather.worst_power(base, exp))

base = 10
exp = 5
print(Mather.worst_power(base, exp))

