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
 
c = cv2.VideoCapture(0)
_,f = c.read()
 
avg1 = np.float32(f)
#avg2 = np.float32(f)
 
while(1):
    _,f = c.read()
     
    cv2.accumulateWeighted(f,avg1,0.000001)
     
    res1 = cv2.convertScaleAbs(avg1)

    diffmask=cv2.absdiff(res1,f)

    diffmask[:,1]=0
    diffmask[:,0]=0





    greyimg = cv2.cvtColor(diffmask, cv2.COLOR_RGB2GRAY)
    blurredimg=cv2.blur(greyimg,(3,3))
    ret,mask=cv2.threshold(blurredimg,30, 255, cv2.THRESH_BINARY)


    #cv2.imshow('img',f)
    #cv2.imshow('background',res1)
    cv2.imshow('differenc',mask)

    k = cv2.waitKey(20)
 
    if k == 27:
        break
 
cv2.destroyAllWindows()
c.release()