# this one is like your scripts with argv
# 定义一个有不确定几个参数的函数
def print_two(*args):
	# 定义两个变量接收参数
    arg1, arg2 = args
    # 打印变量的内容
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print("I got nothing'.")


# 调用函数并传递参数
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()