
nums = []

while True:
    num = input("Enter the number; ")

    if num == 'exit':
        print("loading results.....")
        break
    else:
        nums.append(int(num))

try:
    largest_num = nums[0]
    smallest_num = nums[0]

    for i in nums:
        if i > largest_num:
            largest_num=i
        elif i < smallest_num:
            smallest_num=i

    print(largest_num)        
    print(smallest_num)
except IndexError:
    print("bye")