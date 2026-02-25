# 2026-02-25：本地 push 测试成功！重新启程

import random

# 你的单词小库（随时可以加）
words = [
    ("synthetic", "合成的、人造的"),
    ("perennial", "长期的、持久的"),
    ("artificial", "人造的、假的"),
    ("cognition", "认知、认识过程"),
    ("evolution", "进化、演化"),
    ("wakeup","醒来、觉醒")
]

# 随机挑一个
word, meaning = random.choice(words)

print("今天要碰的单词是：")
print(f"  {word}")
print(f"  意思：{meaning}")

input("\n按回车结束今天的‘学习仪式’～")
print("已完成！明天见～")