offset = int(input("Enter the max number - 1 to 1000::\n"))

print(type(offset))
# total = 0
#
# for num in range(1, offset + 1):
#     # print(num)
#     if num % 2 == 0:
#         total += num
#
# print(total)

total_sum = 0
for n in range(2, offset + 1, 2):
    total_sum += n

print(total_sum)
