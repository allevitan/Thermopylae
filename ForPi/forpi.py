import cv2
import numpy as np
import time
from multiprocessing import Process, Queue

print 'start  ', time.clock()
ServoBlaster = open('/dev/servoblaster', 'w')

print 'FindVictim  ', time.clock()
def FindVictim():
     
    while(1):

        cap = cv2.VideoCapture(-1)
        _,f = cap.read()
        avg1 = np.float32(f)
        print 'got video  ', time.clock() 

        hsvimg = cv2.cvtColor(f, cv2.COLOR_RGB2HSV)
        [H,S,V]=cv2.split(hsvimg)
        print 'split into HSV  ', time.clock()

        cv2.accumulateWeighted(hsvimg,avg1,0.01)
        print 'Averaged  ', time.clock()

        hsvres1 = cv2.convertScaleAbs(avg1)

        [Havg,Savg,Vavg]=cv2.split(hsvres1)
        print 'Average split into HSV', time.clock()

        diffmask1=cv2.absdiff(Havg,H)
        diffmask2=cv2.absdiff(Vavg,V)
        diffmask3=cv2.absdiff(Savg,S)
        print 'diffmasks made  ', time.clock()

        hthresh=int(25.0-(float(np.amin(Havg))*0.22988))
        if hthresh <0:
            hthresh=0
        print 'threshold found  ', time.clock()

        #blurredimg1=cv2.blur(diffmask1,(7,20))
        #blurredimg2=cv2.blur(diffmask2,(7,20))
        #blurredimg3=cv2.blur(diffmask3,(7,20))
        #print 'blurred  ', time.clock()
        ret,mask2=cv2.threshold(blurredimg2,30, 255, cv2.THRESH_BINARY) #h=5 blurry h=20 or more crisp

        ret,mask1=cv2.threshold(blurredimg1,hthresh, 255, cv2.THRESH_BINARY) #v=30
        ret,mask3=cv2.threshold(blurredimg3,35, 255, cv2.THRESH_BINARY) #s=35

        print 'masks made  ', time.clock()
        maska=cv2.add(mask1,mask2)
        mask=cv2.add(maska,mask3)
        print 'masks added ', time.clock()


        contours2,hyerarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print 'contours found  ', time.clock()

        possibleparts=[]
        targets=[]
        looplen=0
        if len(contours2)> 5:
            looplen=5
        else:
            looplen=len(contours2)
        for i in range(looplen):

            cnt2=contours2[i]
            x,y,w,h = cv2.boundingRect(cnt2)

            area=h*w
            ratio=float(w)/float(h)

            if ((area >1000)):# and (ratio >0.2) and ratio <0.6):
                possibleparts.append([x,y,w,h])
                if ((area>4000 and ratio >0.2 and ratio <0.7)):
                    cv2.rectangle(mask2,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),2)
                    targets.append((x-w)/2)
            for j in range(len(possibleparts)):
                for k in range(len(possibleparts)-1):
                    k=k+1
                    x1=possibleparts[j][0]
                    y1=possibleparts[j][1]
                    w1=possibleparts[j][2]
                    h1=possibleparts[j][3]
                    x2=possibleparts[k][0]
                    y2=possibleparts[k][1]
                    w2=possibleparts[k][2]
                    h2=possibleparts[k][3]
                    if ((abs((y1+h1)-y2) <30) or (abs((y2+h2)-y1) <30) and (abs(x1-x2)<60)):
                        if x1 > x2:
                            xnew=x2
                            wnew=x1+w1
                        else: 
                            xnew=x1
                            wnew=x2+w2

                        if y1 > y2:
                            ynew=y2
                            hnew=y1+h1
                        else :
                            ynew=y1
                            hnew=y2+h2

                        ratio=abs(float(xnew-wnew)/float(ynew-hnew))
                        if (ratio >0.2 and ratio <0.6):
                            cv2.rectangle(f,(xnew,ynew),(wnew,hnew),(0,255,0),2)  
                            targets.append((xnew-wnew)/2)
        print 'targets found ', time.clock()
        if len(targets)>0:
            target=targets[0]
            DestroyVictims(target)


def DestroyVictims(target):
    servo1pos=0.3125*target+50
    if servo1pos > 250:
        servo1pos=250
    if servo1pos < 0:
        servo1pos=0
    ServoBlaster.write('0=' + str(servo1pos) + '\n')
    print 'Wrote to servo ', time.clock()

FindVictim()



