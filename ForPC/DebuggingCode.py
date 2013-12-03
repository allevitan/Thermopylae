import cv2
import numpy as np
import time
 
cap = cv2.VideoCapture('colortestcomp.avi')
_,f = cap.read()
 
avg1 = np.float32(f)
counter=0
counter=0
 
while(1):
    counter=counter+1
    _,f = cap.read()

    hsvimg = cv2.cvtColor(f, cv2.COLOR_RGB2HSV)
    [H,S,V]=cv2.split(hsvimg)

    #smallimg2=cv2.convertScaleAbs(hsvimg,scale=2.0)


    cv2.accumulateWeighted(hsvimg,avg1,0.01)

    hsvres1 = cv2.convertScaleAbs(avg1)



    [Havg,Savg,Vavg]=cv2.split(hsvres1)

    #print np.amax(Havg), ' ', np.amin(Havg)


    diffmask1=cv2.absdiff(Havg,H)
    diffmask2=cv2.absdiff(Vavg,V)
    diffmask3=cv2.absdiff(Savg,S)

    hthresh=int(25.0-(float(np.amin(Havg))*0.22988))
    if hthresh <0:
        hthresh=0

    print np.amax(Havg), ' ', np.amin(Havg), ' ', hthresh

    #blurredimg1=cv2.blur(diffmask1,(7,20))
    #blurredimg2=cv2.blur(diffmask2,(7,20))
    #blurredimg3=cv2.blur(diffmask3,(7,20))
    ret,mask2=cv2.threshold(diffmask2,30, 255, cv2.THRESH_BINARY) #h=5 blurry h=20 or more crisp

    ret,mask1=cv2.threshold(diffmask1,hthresh, 255, cv2.THRESH_BINARY) #v=30
    ret,mask3=cv2.threshold(diffmask3,35, 255, cv2.THRESH_BINARY) #s=35
    maska=cv2.add(mask1,mask2)
    mask=cv2.add(maska,mask3)

    erodeelem2=cv2.getStructuringElement(cv2.MORPH_RECT,(1,2))
    maskeroded2=cv2.erode(mask,erodeelem2)
    




    contours2,hyerarchy=cv2.findContours(maskeroded2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    possibleparts=[]
  

    for i in range(len(contours2)):

        cnt2=contours2[i]
        x,y,w,h = cv2.boundingRect(cnt2)

        area=h*w
        ratio=float(w)/float(h)
        

        #if (((ratio<0.5)and(ratio >0.3)) and (area>1000) and (y+h>200)):

            #cv2.rectangle(mask2,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.rectangle(f,(x,y),(x+w,y+h),(184,182,88),2)
            #center=(((x-w)/2),((y-h)/2))
            #print center
        if ((area >1000)):# and (ratio >0.2) and ratio <0.6):
            possibleparts.append([x,y,w,h])
            #cv2.rectangle(f,(x,y),(x+w,y+h),(0,0,155),2)
            if ((area>4000 and ratio >0.2 and ratio <0.7)):
                cv2.rectangle(mask2,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),2)
                center=(((x-w)/2),((y-h)/2))
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
                    #cv2.rectangle(f,(x1,y1),(x1+w1,y1+h1),(0,100,100),2)
                    #cv2.rectangle(f,(x2,y2),(x2+w2,y2+h2),(0,100,0),2)
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
            #print center

    cv2.imshow("Mask",mask)
    cv2.imshow("V",mask2)
    cv2.imshow("H",mask1)
    cv2.imshow("S",mask3)
    # cv2.imshow("Video",f)
    #time.sleep(.1)
    # cv2.imshow("img1",smallimg1)
    # cv2.imshow("img2",smallimg2)
    #cv2.imshow("blue",hsvimg)
    #cv2.imshow("H",H)
    #cv2.imshow("S",S)
    #cv2.imshow("V",V)

    key = cv2.waitKey(20)
 
    if key == 27:
        break
 
cv2.destroyAllWindows()
c.release()