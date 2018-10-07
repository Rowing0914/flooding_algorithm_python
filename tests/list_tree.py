relations = [0,
			[1,[3,4]],
			[2,[5,6]]
			]

def level_check(l, level):
	level += 1
	for i in l:
		if type(i) == list:
			level_check(i, level)
		else:
			print("Level: %d, value: %d"%(level, i))

level_check(relations, -1)