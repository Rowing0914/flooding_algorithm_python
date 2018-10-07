import time
import tkinter as tk

# initialise the window of the canvas
animation = tk.Tk()
canvas = tk.Canvas(animation, width=400, height=350)
canvas.pack()

PROCESS_RADIUS    = 10
MESSAGE_RADIUS    = 3
ANIMATION_DELAY   = 10
SLEEPTIME         = 0.3
INITIAL_COLOUR    = 'red'
TERMINATED_COLOUR = 'green'

class Process:
	def __init__(self, x, y, radius, colour, pid=0, level=0):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.core = canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill=self.colour)
		self.children = []
		self.parent = 0
		self.pid = pid
		self.level = 0

	def change_colour(self):
		"""
		changing the colour when the transition happens
		"""
		canvas.itemconfig(self.core, fill=TERMINATED_COLOUR)

def multi_send(Tree, list_from, list_to):
	"""
	sending messages
	"""
	# store all msgs
	messages = {}

	# define parent and child to pass information among them
	for index, (_from, _to) in enumerate(zip(list_from, list_to)):
		# calculate the length of travel
		path_x, path_y = (Tree["p_"+str(_to)].x - Tree["p_"+str(_from)].x)/ANIMATION_DELAY, (Tree["p_"+str(_to)].y - Tree["p_"+str(_from)].y)/ANIMATION_DELAY

		# store all msgs
		messages["mes_"+str(index)] = {"object": Process(Tree["p_"+str(_from)].x, Tree["p_"+str(_from)].y, MESSAGE_RADIUS, 'blue'), 
									   "path_x": path_x,
									   "path_y": path_y}
	print(messages)

	# update the canvas by moving the objects gradually
	for j in range(ANIMATION_DELAY):
		for index in range(len(list_to)):
			mes, path_x, path_y = messages["mes_"+str(index)]['object'], messages["mes_"+str(index)]['path_x'], messages["mes_"+str(index)]['path_y']
			canvas.move(mes.core, path_x, path_y)
		animation.update()
		time.sleep(SLEEPTIME)

	# change the colour of the process which finishes a computing phase
	for index in list_to:
		Tree["p_" + str(index)].change_colour()
	animation.update()

def tree_construction(l, level, Tree):
	"""
	construct tree
	"""
	level += 1
	for unit in l:
		if type(unit) == list:
			tree_construction(unit, level, Tree)
		else:
			pid, x, y, radius, colour = unit
			Tree["p_"+str(pid)] = Process(x, y, radius, colour, pid, level)


def flatten(l, result):
	"""
	flatten a list
	"""
	for i in l:
		if type(i) == list:
			flatten(i, result)
		else:
			result.append(i)
	return result

if __name__ == '__main__':
	# processes
	data =  [(0, 200, 30,  PROCESS_RADIUS, INITIAL_COLOUR),
			[(1, 170, 120, PROCESS_RADIUS, INITIAL_COLOUR),[(3, 130, 260, PROCESS_RADIUS, INITIAL_COLOUR),(4, 180, 260, PROCESS_RADIUS, INITIAL_COLOUR)]],
			[(2, 230, 120, PROCESS_RADIUS, INITIAL_COLOUR),[(5, 220, 260, PROCESS_RADIUS, INITIAL_COLOUR),(6, 270, 260, PROCESS_RADIUS, INITIAL_COLOUR)]]
			]

	# relationship among processes
	relations = ["0-1",
				 "0-2",
				 "1-3",
				 "1-4",
				 "2-5",
				 "2-6"]

	# £ of nodes in the layer
	layer_nodes = [1,2,4]

	Tree = {}

	# construct the tree based on data
	tree_construction(data, -1, Tree)
	print(Tree)
	
	for relation in relations:
		parent, child = relation.split("-")

		# register children to the parent process
		Tree["p_"+str(parent)].children.append(child)
		# register the parent to children
		Tree["p_"+str(child)].parent = parent
		
		# draw lines to connect nodes and construct a tree on the map
		canvas.create_line(Tree["p_"+str(parent)].x, Tree["p_"+str(parent)].y, Tree["p_"+str(child)].x, Tree["p_"+str(child)].y)

	# for a in Tree
	print("<< processes on the map >>\n", Tree)
	
	sending_order = []
	list_from, list_to = [], []
	count = 0

	# creating the order of delivery
	for item in layer_nodes[:-1]:
		for i in range(item):
			list_from.append([Tree["p_"+str(count)].pid for i in range(len(Tree["p_"+str(count)].children))])
			list_to.append(list(map(int, Tree["p_"+str(count)].children)))
			count += 1
		list_from = flatten(list_from, [])
		list_to = flatten(list_to, [])
		sending_order.append((list_from, list_to))
		list_from, list_to = [], []
	
	print(sending_order)

	# sending forward
	for i in sending_order:
		print("i: ", i)
		list_from, list_to = i
		multi_send(Tree, list_from, list_to)
	
	# sending backward
	for i in sending_order[::-1]:
		list_from, list_to = i
		multi_send(Tree, list_to, list_from)