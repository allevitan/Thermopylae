# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)


# while(1):
#     ret, frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     print(fgmask.shape)
#     greyimg = cv2.cvtColor(cap.read[1], cv2.COLOR_RGB2GRAY)

#     print(fgmask[30:2])

#     cv2.imshow('frame',greyimg)
#     k = cv2.waitKey(30) & 0xff

#     if k == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
_,f = cap.read()
 
avg1 = np.float32(f)
#avg2 = np.float32(f)
 
while(1):
    _,f = cap.read()
     
    cv2.accumulateWeighted(f,avg1,0.01)
     
    res1 = cv2.convertScaleAbs(avg1)

    diffmask=cv2.absdiff(res1,f)

    diffmask[:,1]=0
    diffmask[:,0]=0





    greyimg = cv2.cvtColor(diffmask, cv2.COLOR_RGB2GRAY)
    blurredimg=cv2.blur(greyimg,(3,3))
    ret,mask=cv2.threshold(blurredimg,20, 255, cv2.THRESH_BINARY)

    erodeelem=cv2.getStructuringElement(cv2.MORPH_RECT,(4,4))
    maskeroded=cv2.erode(mask,erodeelem)
    maskeroded_1=maskeroded



    contours,hyerarchy=cv2.findContours(maskeroded,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(maskeroded,contours,-1,(0,255,0),3)
    #rect=cv2.boundingRect(contours)
    areas = [cv2.contourArea(c) for c in contours]
    if len(areas)>0:
        max_index = np.argmax(areas)
        cnt=contours[max_index]

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(mask,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Show",mask)

    #cv2.imshow('img',f)
   # cv2.imshow('background',maskeroded)
    #cv2.imshow('differenc',maskeroded_1)

    k = cv2.waitKey(20)
 
    if k == 27:
        break
 
cv2.destroyAllWindows()
c.release()