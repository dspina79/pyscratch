def generator_method():
    print('Sending out the first')
    yield 1

    print('Sending out the second item')
    yield 2

    print('Sending out the third item')
    yield 3

it1 = generator_method()
x = next(it1)
print(x)
x = next(it1)
print(x)

def fibonacci():
    x = 0
    y = 1
    for i in range(0, 40):
        yield y
        temp = y
        y = x + y
        x = temp

fibit = fibonacci()
print(next(fibit))
print(next(fibit))
print(next(fibit))
print(next(fibit))
print(next(fibit))
print(next(fibit))

