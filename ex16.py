# 从sys导入argv
from sys import argv
# 定义两个变量用于接收解压argv获取的值
script, filename = argv

print("We're going to erase %r ." % filename)
print("If you don't want that , hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
# 定义一个变量用来接收以写的方式打开文件中的内容
target = open(filename, 'w')

print("Truncating the file. Goodbye")
# 清空文件中内容
target.truncate()

print("Now I'm going to ask you for three lines.")
# 定义一个变量用于接收输入的内容
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# 将输入的内容写入到文件中
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# 关闭文件
target.close()