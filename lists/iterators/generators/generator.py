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