import threading
import cv2
from collections import deque
import time

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
        while vid.isOpened():
            #time.sleep(3)
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