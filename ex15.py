# 从sys中导入argv
from sys import argv

# 给argv解压并把值赋值给两个变量
script, filename = argv

# 定义一个变量用来接收打开文件的内容
txt = open(filename)
# 打印文件名
print("Here's your file %r:" % filename)
# 打印文件中的内容
print(txt.read())
txt.close()


# 再次输入文件名
print("Type the filename again:")
# 定义一个变量它的值等于输入的内容

file_again = filename #input("> ")
print(filename)

# 定义一个变量用于接收打开输入文件命中的内容
txt_again = open(file_again)

# 打印再次输入文件名中的内容
print(txt_again.read())

txt_again.close()