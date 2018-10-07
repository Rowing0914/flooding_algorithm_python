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
	def __init__(self, x, y, radius, colour, pid=0):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = colour
		self.core = canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius, fill=self.colour)
		self.children = []
		self.parent = 0
		self.pid = pid
		self.layer = 0

	def change_colour(self):
		canvas.itemconfig(self.core, fill=TERMINATED_COLOUR)

# Deprecated 
# def send():
# 	mes1 = Process(Tree["p_"+str(0)].x, Tree["p_"+str(0)].y, MESSAGE_RADIUS, 'blue')
# 	mes2 = Process(Tree["p_"+str(0)].x, Tree["p_"+str(0)].y, MESSAGE_RADIUS, 'blue')
	
# 	path_x1, path_y1 = (Tree["p_"+str(0)].x - Tree["p_"+str(1)].x)/ANIMATION_DELAY, (Tree["p_"+str(1)].y - Tree["p_"+str(0)].y)/ANIMATION_DELAY
# 	path_x2, path_y2 = (Tree["p_"+str(0)].x - Tree["p_"+str(2)].x)/ANIMATION_DELAY, (Tree["p_"+str(2)].y - Tree["p_"+str(0)].y)/ANIMATION_DELAY

# 	for j in range(ANIMATION_DELAY):
# 		canvas.move(mes1.core, path_x1, path_y1)
# 		canvas.move(mes2.core, path_x2, path_y2)
# 		animation.update()
# 		time.sleep(SLEEPTIME)

# Unit test purpose: you can send the info from _from process to _to process
# def _send(_from, _to):
# 	mes = Process(Tree["p_"+str(_from)].x, Tree["p_"+str(_from)].y, MESSAGE_RADIUS, 'blue')
	
# 	path_x, path_y = (Tree["p_"+str(_from)].x - Tree["p_"+str(_to)].x)/ANIMATION_DELAY, (Tree["p_"+str(_to)].y - Tree["p_"+str(_from)].y)/ANIMATION_DELAY

# 	for j in range(ANIMATION_DELAY):
# 		canvas.move(mes.core, path_x, path_y)
# 		animation.update()
# 		time.sleep(SLEEPTIME)

def multi_send(Tree, list_from, list_to):
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


if __name__ == '__main__':
	data = [[200, 30,  PROCESS_RADIUS, INITIAL_COLOUR],
			[170, 120, PROCESS_RADIUS, INITIAL_COLOUR],
			[230, 120, PROCESS_RADIUS, INITIAL_COLOUR],
			[130, 260, PROCESS_RADIUS, INITIAL_COLOUR],
			[180, 260, PROCESS_RADIUS, INITIAL_COLOUR],
			[220, 260, PROCESS_RADIUS, INITIAL_COLOUR],
			[270, 260, PROCESS_RADIUS, INITIAL_COLOUR]]

	relations = ["0-1",
				 "0-2",
				 "1-3",
				 "1-4",
				 "2-5",
				 "2-6"]

	Tree = {}

	# instantiate all processes
	for index, unit in enumerate(data):
		x, y, radius, colour = unit
		Tree["p_"+str(index)] = Process(x, y, radius, colour, pid=index)
	
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

	list_from, list_to = [0,0], [1,2]
	multi_send(Tree, list_from, list_to)

	list_from, list_to = [1,1,2,2], [3,4,5,6]
	multi_send(Tree, list_from, list_to)

	list_from, list_to = [3,4,5,6], [1,1,2,2]
	multi_send(Tree, list_from, list_to)

	list_from, list_to = [1,2], [0,0]
	multi_send(Tree, list_from, list_to)
