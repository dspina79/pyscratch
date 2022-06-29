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

    p2 = MyProcess(2)
    p2.start()

