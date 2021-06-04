from flask import Flask,request
import cv2
import pickle
import time
from collections import deque
import threading
qu=deque()
def insertTheFrame(frame):
    print('inserting the frame')
    if len(qu)>=50:
        for i in range(50-2):
            qu.popleft()
            print('recalibrating the frame')
    qu.append(frame)

def readFrame():
    while len(qu)==0:
        continue
    return qu.popleft()
class Framedisplay(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            if len(qu)==0:
                #print('no elements in the queue')
                continue
            else:
                print('diplaying frame')
                #display this frame
                print('the frame is ')
                r=readFrame()
                print(r,flush=True)
                #if r==None:
                #    continue
                cv2.imshow('frame from the server',r)
            if cv2.waitKey(1) & 0xFF == ord('q'): #latter we have to find some different closing mechanism.
                break
        cv2.destroyAllWindows()

app = Flask(__name__, template_folder='./')

@app.route('/frame',methods = ['POST', 'GET'])
def frame():
    t=request.data
    t=pickle.loads(t)
    insertTheFrame(t)   
    #print('shown')
    return "this" 

if __name__ == '__main__':
    Framedisplay().start()
    print('other thread also started')
    app.run(debug = False,host='127.0.0.1',port=5000)  