import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self, id):
        super(MyProcess, self).__init__()
        self.id = id
    
    def run(self):
        time.sleep(self.id)
        print("The proocess is running with id", self.id)


if __name__ == '__main__':
    p1 = MyProcess(1)
    p1.start()
    p1.join()
    p2 = MyProcess(5)
    p2.start()
    p2.join() # makes it synchronous

    p3 = MyProcess(3)
    p4 = MyProcess(3)
    p3.start()
    p4.start()