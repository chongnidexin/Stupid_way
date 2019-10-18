def add(a, b):
    """定义加法函数"""


print("ADDING %d + %d " % (a, b))
return a + b


def subtract(a, b):
    """定义减法函数"""


print("SUBTRACTING %d -%d" % (a, b))
return a - b


def multiply(a, b):
    """定义乘法函数"""


print("MULTIPLYING %d * %d " % (a, b))
return a * b


def divide(a, b):
    """定义除法函数"""


print("dividing %d / %d " % (a, b))
return a / b

print("Let's do some math with just functions ")
# 调用函数病传递参数并定义变量来接收
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))
