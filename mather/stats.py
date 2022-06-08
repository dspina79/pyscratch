def generate_average(nums):
    n = nums.__len__()
    total = 0
    if n == 0:
        return None
    else:
        for x in nums:
            total += x
        return total / n

nums = []
while True:
    current_intput = input("Get a number or blank to end: ")
    if current_intput == "":
        break
    else: 
        nums.append(int(current_intput))

avg = generate_average(nums)
print("The average is", avg)
