def generate_average(nums):
    n = nums.__len__()
    total = 0
    if n == 0:
        return None
    else:
        for x in nums:
            total += x
        return total / n

def std_dev(nums):
    n = nums.__len__()
    if n == 0:
        return None
    else:
        avg = generate_average(nums)
        numerator = 0
        for n in nums:
            numerator = (n - avg) ** 2
        quot = numerator / nums.__len__()
        return quot ** (1/2)


nums = []
while True:
    current_intput = input("Get a number or blank to end: ")
    if current_intput == "":
        break
    else: 
        nums.append(int(current_intput))

avg = generate_average(nums)
print("The average is", avg)
stddev = std_dev(nums)
print("The standard deviation is", stddev)