my_list = [1,2,3,4,5,6]
my_it = iter(my_list)

print(next(my_it))
print(next(my_it))
print(next(my_it))

print(my_list)

print(next(my_it))

print('Adding a new number')
my_list.append(7)
print(my_list)


print(next(my_it))
print(next(my_it))
print(next(my_it))

# the following would fail because of the StopIteration exception
#print(next(my_it)) 

my_list2 = ['a', 'b', 'c', 'd', 'e']

my_it2 = iter(my_list2)

while True:
    try:
        print(next(my_it2))
    except StopIteration:
        print('No more elements')
        break



