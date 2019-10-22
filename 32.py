# 定义列表
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


# this first kind of for-loop goes through a list
# 遍历数字列表
for number in the_count:
	# 打印是第几次计数
	print("This is count %d " % number)

# same as above
# 遍历水果列表
for fruit in fruits:
	# 打印水果的名字
	print("A fruit of type: %s " % fruit)



# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in ti 
# 遍历列表
for i in change:
	# 打印列表中的内容
	print("I got %r " % i)


# we can slso build lists, first start with an empty one
# 定义一个空列表
elements =[]


# then use the range function to do 0 to 5 counts
# 遍历1到5
for i in range(0,6):
	# 打印值
	print("Adding %d to the list." %i)
	# append is a function that lists understand
	# 将得到的值追加入列表中
	elements.append(i)


# now wencan print them out to
# 遍历elements列表 
for i in elements:
	# 打印elements中的值
	print("Element was: %d" % i)
