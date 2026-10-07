nums = []

while True:
    num = input("Enter The Number: ")

    if num == 'exit':
        break
    else:
        nums.append(int(num))

positive = 0
negative = 0
zero = 0
sum = 0

for i in nums:
    if i > 0:
        positive += 1
        sum += i
    elif i < 0:
        negative += 1
    else:
        zero += 1


print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zeros: {zero}")
print(f"Positive sum: {sum}")