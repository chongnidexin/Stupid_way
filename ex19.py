# 定义一个两个参数的函数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # 打印
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# 调用函数并传递参数
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")

# 定义一个变量赋值为10
amount_of_cheese = 10
# 定义一个变量赋值为50
amount_of_crackers = 50

# 调用函数并传递参数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")

cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# 调用函数并传递参数进行计算
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
