# # 练习1（if-elif-else）：
# 输入一个年龄，如果年龄 >= 18，打印 "Adult"；
age = int(input("请输入年龄: "))

if age >= 18:
    print("Adult")
# 如果年龄 >= 13，打印 "Teenager"；
elif age >= 13:
    print("Teenager")
# 否则打印 "Child"。
else:
    print("Child")

# 练习2（多个 if）：
# 输入一个数字，如果是偶数，打印 "Even"；
number = int(input("Enter a number:"))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 如果大于 100，打印 "Big number"；
if number > 100:
    print("Big number")
# （注意：这两个条件可以同时成立）

# 练习3（if-else）：
# 输入考试分数（0-100），如果 >= 60，打印 "Pass"，否则打印 "Fail"。
score = float(input("输入考试分数："))

if score < 0:
    exit(0)
if score >= 60:
    print("pass")
else:
    print("fail")

# 闰年和平年的计算公式
year = int(input("输入年份："))

if year < 1852:
    print("Not within the Gregorian calendar period.")
elif year % 4 != 0:
    print("common year")
elif year % 100 != 0:
    print("leap year")
elif year % 400 != 0:
    print ("common year")
else:
    print("leap year")

# if-elif-else练习
num = float(input("enter a number:"))

if num > 100:
    print("Very Big")
elif num > 50:
    print("Big")
elif num > 0:
    print("Positive")
else:
    print("Non Positive")

# 修改税费题（增加收入<=0,tax=0)
income = float(input("Enter an annual income:"))

if income <= 0:
    tax = 0
elif income < 85528:
    tax = income  * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

tax = round(tax,0)
print("the tax is:", tax, "thalers")
