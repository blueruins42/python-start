# while-if
largest_number = -99999999

number = int(input("Enter a value:"))

while number != -1: # 负责循环一段代码，被循环部分必须缩进一样的距离
    if number > largest_number:
        largest_number = number   # 条件满足才执行，否则跳过
    number = int(input("Enter a new value:"))  # 直到输入-1才结束循环
print("THe largest number is:", largest_number)

# while
counter = 5
while counter != 0:
    print("inside the loop", counter)
    counter -= 1
print("outside the loop", counter)

# while-if-else
total = 0      # 用来累加所有正整数的总和
count = 0      # 用来记录输入了多少个有效正整数

# 第一次输入放在循环外面
number = int(input("Enter a positive integer (-1 to stop): "))

while number != -1:
    if number > 0:
        total += number        # 累加
        count += 1             # 计数
    else:
        print("Please enter a positive number!")
    
    # 每次循环结束前，必须重新输入
    number = int(input("Enter a positive integer (-1 to stop): "))

# 循环结束后，才打印结果
if count > 0:
    average = total / count
    average = round(average, 2)
    print("The sum is:", total)
    print("The average is:", average)
else:
    print("No numbers were entered.")

# for
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power) # 顺序不能随意调换，否则引起错位
    power *= 2

