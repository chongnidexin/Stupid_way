# 从sys中到入argv
from sys import argv

# 用两个变量来接收解压argv获取到的值
script, input_file = argv


# 定义一个带参数的函数
def print_all(f):
    # 打印已读取参数文件获取到的内容
    print(f.read())


# 定义一个带参数的函数
def rewind(f):
    # 移动文件读取指针到指定0位置。
    f.seek(0)


# 定义一个携带两个参数的函数
def print_a_line(line_count, f):
    # 打印参数内容，及文件某一行内容
    print(line_count, f.readline())


# 定义一个变量用于接收打开文件获取到的内容
current_file = open(input_file)
print("First let's print the whole file: \n")
# 调用函数并传递参数（打开文件获取到的内容）
print_all(current_file)

# 调用移动文件指针到0位置函数并传递打开文件获取到的文件内容
rewind(current_file)

print("Let's print three lines: ")
# 定义一个变量赋值为1
current_line = 1

print_a_line(current_line, current_file)

current_line = current_line + 1

print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
