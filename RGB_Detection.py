import cv2
import numpy as np
cap=cv2.VideoCapture(0)

red_LR=np.array([126,188,47])
red_UR=np.array([179,255,255])
def red(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,red_LR,red_UR)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    n = []
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            x1 = int(x+x+w)//2
            y1 = int(y+y+h)//2
            n.append(x)
            cv2.circle(img,(x1,y1),4,(255,255,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,("Red"),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    r = len(n) 
    cv2.putText(frame,("Total Red objecjects : " + str(r)),(10,15),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)


green_LR=np.array([66,155,40])
green_UR=np.array([98,255,255])
def green(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,green_LR,green_UR)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    n = []
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            x2 = int(x+x+w)//2
            y2 = int(y+y+h)//2
            n.append(x)  
            cv2.circle(img,(x2,y2),4,(255,255,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("Green"),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
    g = len(n)
    cv2.putText(frame,("Total Green objects : " + str(g)),(10,35),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)

blue_LR=np.array([88,176,70])
blue_UR=np.array([133,255,255])
def blue(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,blue_LR,blue_UR)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    n = []
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            x3 = int(x+x+w)//2
            y3 = int(y+y+h)//2
            n.append(x)
            cv2.circle(img,(x3,y3),4,(255,255,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,("blue"),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
    b = len(n)
    cv2.putText(frame,("Total Blue objects : " + str(b)),(10,55),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)


while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    red(frame)
    green(frame)
    blue(frame)
            
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()