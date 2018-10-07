from multiprocessing import Pool
import multiprocessing as multi
from joblib import Parallel, delayed
import time
import random

class temp:
    def __init__(self):
        print("I'm born!")

def process(n, temp):
    time.sleep(random.randint(0,3))
    print(temp())
    print("processing_%d"%n)

if __name__ == '__main__':
    Parallel(n_jobs=-1)([delayed(process)(n, temp) for n in range(2)])

    # p = Pool(multi.cpu_count())
    # p.map(process, [0,1])
    # p.close()