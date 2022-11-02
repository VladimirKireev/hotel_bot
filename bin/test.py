test_list = [3, 'f', 2, 's']
res = 0

for i in test_list:
	try:
		res += i
	except TypeError:
		pass

print(res)
