# self 对象的代称，占位符，随时会被真创建的对象替换，保证代码独立互不影响
class Stack:                 # 定义"栈"这个类别（图纸，还不是真抽屉）
    def __init__(self):      # 造实例时自动跑的"初始化函数"
        self.stack_list = [] # 给这个对象装一个空格子（≈ 过程式 stack_list=[]，但挂在对象上）

stack_object = Stack()       # 右边造一个真对象，左边贴名字 stack_object；
                             # 这步自动触发上面 __init__，self 就是刚造的真对象
print(len(stack_object.stack_list))  # stack_object.stack_list 就是那个空格子，len=0 → 打印 0

# Excuction order:1 
class Stack:   
    def __init__(self):
        self.__stack_list = []

# Excuction order: 3
    def push(self, val):
        self.__stack_list.append(val) 

# Excuction order: 5
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

# Excuction order:2
stack_object.push(3)  # [3]
stack_object.push(2)  # [3,2]
stack_object.push(1)  # [3,2,1]

# Excuction order: 4
print(stack_object.pop())  # [1]
print(stack_object.pop())  # [2]
print(stack_object.pop())  # [3]

# two stacks
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object_1 = Stack()  # []
stack_object_2 = Stack()  # []

stack_object_1.push(3)  # stack_object_1 = [3], stack_object_2 = []
stack_object_2.push(stack_object_1.pop())  # first pop →stack_object_1 = [], return val 3, then push stack_object_2 = [3]

print(stack_object_2.pop())  # 3

# three stacks
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


little_stack = Stack()  # []
another_stack = Stack()  # []
funny_stack = Stack()  # []

little_stack.push(1)  # little_stack = [1], another_stack = [], funny_stack = []
another_stack.push(little_stack.pop() + 1)  # little_stack = [], another_stack = [1+1], funny_stack = []
funny_stack.push(another_stack.pop() - 2) # little_stack = [], another_stack = [], funny_stack = [1+1-2]

print(funny_stack.pop()) # 0

# construct a subclass of the already existing Stack class
# define a new subclass pointing to the class which will be used as the superclass.
class AddingStack(Stack):
    pass

# Python forces you to explicitly invoke a superclass's constructor
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


 
