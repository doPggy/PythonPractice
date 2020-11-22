# coding:utf-8
# 第15课 Python对象比较、拷贝

import copy

if __name__ == "__main__":
	l1 = [2222, [1, 22], 2, 3, '111', (1, 2)]
	l2 = copy.deepcopy(l1)

	print(l1 == l2)
	print(l1 is l2)

	print(l1[0] is l2[0])
	# 证明数字，字符串等不可变对象创建后只有唯一引用的数据，深拷贝也只是返回唯一
	print(l1[-2] is l2[-2])
	# 元组的拷贝始终唯一
	print(l1[-1] is l2[-1])
	# list	
	print(l1[1] is l2[1])

	t1 = (100000, 1000)
	t2 = copy.deepcopy(t1)
	print(t1 is t2)