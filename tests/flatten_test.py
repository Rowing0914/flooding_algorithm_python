def _flatten(l, result):
	for i in l:
		if type(i) == list:
			flatten(i, result)
		else:
			result.append(i)
	return result

def flatten(l):
	for i in l:
		if type(i) == list:
			flatten(i)
		else:
			yield i

a = [[1, 1], [2, 2]]
b = [[3, 4], [5, 6]]
result = []
print(flatten(a))