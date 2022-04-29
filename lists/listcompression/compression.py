names = ["Dean", "Linda", "Kevin", "Shirley", "Adam"]
new_list = [name for name in names if "a" in name ]
print(new_list)

# outputs ['Dean', 'Linda', 'Adam']

nums = [1,2,3,5,8,13,21,34]
evens = [num for num in nums if num % 2 == 0]
print(evens)
# prints [2, 8, 34]