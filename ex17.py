# 从sys导入argv
from sys import argv
# 从os.path 导入exists
from os.path import exists

# 定义三个变量用于接收解压argv得到的值
script, from_file, to_file = argv

# 打印出来是从哪个文件往哪个文件复制内容
print("Copying from %s to %s " % (from_file, to_file))

# we coule do these two on one line too, how?（我们也可以把这两个放在一条线上，怎么样?）
# 定义一个变量用于接收打开from_file获取到的内容
first = open(from_file)
# 定义一个变量用于接收以读的方式获取到的文件内容
indata = first.read()

# 打印文件的的内容长度
print("The input file is %d bytes long" % len(indata))

# 打印检测本地需to_file的文件名是否存在
print("Does the output file exist? %r" % exists(to_file))
# 打印 准备好，按回车继续，CTRL-C终止
print("Ready, hit RETURN TO continue, CTRL-C to abort.")
input()

# 定义一个变量用于接收以写的方式打开要to_file的文件
output = open(to_file, 'w')

print(to_file)
# 将读取from_file的内容写入到to_file的文件中
output.write(indata)
# 文字描述
print("Alright, all done.")

# 关闭打开文件（to_file）
output.close()
# 关闭打开文件（from_file）
first.close()