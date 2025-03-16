student_height = input("Enter the list of height::\n").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

total_height = 0
for height in student_height:
    total_height += height
print(f"Total student height is: {total_height}")

total_student = 0
for student in student_height:
    total_student += 1
print(f"Total student is: {total_student}")

average_height = round(total_height / total_student)
print(f"Average student height is: {average_height}")

# total = 0
# students = len(all_height)
#
# for n in range(0, len(all_height)):
#     all_height[n] = int(all_height[n])
#     total += all_height[n]
#
# average_height = total / students
#
# print(f"Total student height is: {total}")
# print(f"Number of students is: {students}")
# print(f"The average height of student is {round(average_height)}")

