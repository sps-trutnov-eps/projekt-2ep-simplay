import time

class TimeCount():  
    def __init__(self):
        self.f = open('time.txt','r')

    def time(self):
        file = self.f.readlines()
        last = int(file[0])

        #time = 
        self.f.close()
        file = open('time.txt', 'w')
        file.write(str(time))
        file.close()  