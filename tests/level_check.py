relations = [0,
			[1,[3,4]],
			[2,[5,6]]
			]
PROCESS_RADIUS    = 10
INITIAL_COLOUR    = 'red'

data =  [(200, 30,  PROCESS_RADIUS, INITIAL_COLOUR),
		[(170, 120, PROCESS_RADIUS, INITIAL_COLOUR),[(130, 260, PROCESS_RADIUS, INITIAL_COLOUR),(180, 260, PROCESS_RADIUS, INITIAL_COLOUR)]],
		[(230, 120, PROCESS_RADIUS, INITIAL_COLOUR),[(220, 260, PROCESS_RADIUS, INITIAL_COLOUR),(270, 260, PROCESS_RADIUS, INITIAL_COLOUR)]]
		]

def level_check(l, level):
	level += 1
	for index, i in enumerate(l):
		# print(index)
		if type(i) == tuple:
			pass
		else:
			print(len(i))
			print(index)
		if type(i) == list:
			level_check(i, level)
		else:
			print(level, i)

# level_check(relations, -1)
level_check(data, -1)