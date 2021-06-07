import threading
import cv2
from collections import deque
import time

class Resolution:
    def __init__(self):
        self.resolution=40
        self.timeToSleep=1/self.resolution

    def setResolution(self,r):
        self.resolution=r
        #now we need to do little maths.
        #1000ms --- r images
        #1000/r time sleep required
        self.timeToSleep=1/self.resolution

    def sleepResolution(self):
        time.sleep(self.timeToSleep)
        
class localShadow(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.frame=deque() #locking can be used if things fail.
        self.isPresent=False
        self.thres=50

    def getFrame(self):
        l=None
        while l==None or l<=2:
            l=len(self.frame)

        for i in range(l-2):
            self.frame.popleft()#things are happening here
        return self.frame.popleft()

    def isFramePresent(self):
        return self.isPresent

    #execution will start from here    
    def run(self):
        vid = cv2.VideoCapture(0)
        res=Resolution()
        while vid.isOpened():
            #time.sleep(3)
            res.sleepResolution() #this is sleeping to make resoulution go okey
            l=len(self.frame)
            if l>=self.thres:
                for i in range(l-2):
                    self.frame.popleft()


            ret,frame=vid.read()
            if ret==False:
                print('return value is false')
                break
            cv2.imshow('frame', frame)
            #self.frame=frame
            self.frame.append(frame)
            self.isPresent=True
            if cv2.waitKey(1) & 0xFF == ord('q'): #latter we have to find some different closing mechanism.
                break
        vid.release()
        cv2.destroyAllWindows()