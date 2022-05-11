def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    else:
        raise TypeError('Cannot be less than 0')


try:
    print("Factorial(5) = ", factorial(5))
    print("Factorial(1) = ", factorial(1))
    print("Factorial(-12) = ", factorial(-12))
except TypeError:
    print('Type error received.')