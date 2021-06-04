import cv2
import pickle
import requests
from localShadow import localShadow

myshadow=localShadow()
myshadow.start()
while True:
        if myshadow.isPresent==False:
            print('continued')
            continue
    
        t=myshadow.getFrame()
        temp=pickle.dumps(t)
        requests.post('http://127.0.0.1:5000/frame',data=temp)
        #i.e getting the frame and sending it to the server.