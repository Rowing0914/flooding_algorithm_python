import time
import tkinter as tk
from random import randint
from joblib import Parallel, delayed
from multiprocessing import Pool
import multiprocessing as multi

def process(n, canvas):
	print(canvas)
	# canvas.move(target, 3, 5)
	print("processing_%d"%i)
	# canvas.create_oval(randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), fill="green")

if __name__ == '__main__':
	animation = tk.Tk()
	canvas = tk.Canvas(animation, width=400, height=350)
	canvas.pack()

	# for i in range(3):
	# 	process(i)
	# 	animation.update()
	# 	time.sleep(0.5)

	Parallel(n_jobs=2)([delayed(process)(n, canvas) for n in range(2)])
	animation.update()
	time.sleep(0.5)
