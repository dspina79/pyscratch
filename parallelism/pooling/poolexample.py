import multiprocessing
import time

def cube (x):
    return x * x * x

def square(x):
    print("Squaring", x)
    time.sleep(3)
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    inputs = [1,2,4,6,8,9,123]
    outputs = pool.map(cube, inputs)
    outputs_sq = pool.map(square, inputs)
    print("Inputs", inputs)
    print("Outputs Cube", outputs)
    print("Outputs Squared", outputs_sq)

    #items are running is batches of 3 at a time