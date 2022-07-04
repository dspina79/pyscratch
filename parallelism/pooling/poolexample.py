import multiprocessing
import time

def cube (x):
    return x * x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    inputs = [1,2,4,6,8,9,123]
    outputs = pool.map(cube, inputs)
    print("Inputs", inputs)
    print("Outputs", outputs)