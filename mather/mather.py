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
    

x = 10
y = 15
z = 0

print(Mather.add(x, y))
print(Mather.subtract(x, y))
print(Mather.multiply(x, y))
print(Mather.divide(x, y))