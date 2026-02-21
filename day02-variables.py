# Day 2: 变量 + f-string
my_name = "shooting"  #加引号作为string
my_age = 35  #不加引号，作为integer
message = "开始尝试写第一个python语法。"

print(f"我叫{my_name}，刚过完 {my_age} 岁生日，{message}")

# 定义现在的年份（数字，不加引号）
current_year = 2026

# 计算距离 100 岁还有多少年
years_to_wait = 100 - my_age

# 计算那一年的年份
year_of_100 = current_year + years_to_wait

# 把结果印出来
print("当我 100 岁的时候，那是：")
print(year_of_100)
# 另一种用逗号分隔的输出方法
print("当我 100 岁的时候，那是：",year_of_100)
# 另一种用f_string合体的输出方法
print(f"当我 100 岁的时候，那是：{year_of_100}")
