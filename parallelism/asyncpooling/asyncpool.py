import multiprocessing
import time

def cube(x):
    return x * x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)
    inputs = [0,1,5,16,100,256]
    print("This statement is before the mapping")
    outputs_async = pool.map_async(cube, inputs)
    print("This statement is after the mapping")
    print("This statement is before the get")
    outputs_result = outputs_async.get()
    print("This statement is after the get")
    print("Ouputs: ", outputs_result)

    # the above prints

    # This statement is before the mapping
    # This statement is after the mapping
    # This statement is before the get
    # This statement is after the get
    # Ouputs:  [0, 1, 125, 4096, 1000000, 16777216]