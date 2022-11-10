# page start
print()

# varables
num_in = ""
num_list = []
max_num = 0
ave_num = 0
sum_num = 0
in_tf = True

# main code
# list input
print("Enter a list of numbers, type 0 when finished.")
while in_tf:
    num_in = input("Enter number: ")
    num_in = int(num_in)
    if num_in == 0:
        in_tf = False
    else:
        num_list.append(num_in)

# sum of the list
for num in num_list:
    sum_num += num

# average of the list
ave_num = sum_num / len(num_list)

# biggest value in the list
for num in num_list:
    if num > max_num:
        max_num = num

# output
print(f"The sum is: {sum_num}")
print(f"The average is: {ave_num}")
print(f"The largest number is: {max_num}")

# page end
print()
