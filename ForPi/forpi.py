import cv2
import numpy as np
import time
import random
from multiprocessing import Process, Queue
#print 'start  ', time.clock()
ServoBlaster = open('/dev/servoblaster', 'w')
Servo0DP = Queue()	# Servo zero desired position, sent by main and read s
Servo1DP = Queue()	# Servo one desired position, sent by main and read b

def FindVictim():
    counter=0
    targ_counter=0
    prevtarget=100
    fimg=cv2.imread('ftest.png')
    cap = cv2.VideoCapture(-1)
    avg1 = np.float32(fimg) 
    while(1):
#	print 'Start', time.clock()
        _,fbig = cap.read()
	f = fbig
	targ_counter=targ_counter+1
#	print 'targ_counter'
#	print 'got video', time.clock()
	newx,newy=fbig.shape[1]/2,fbig.shape[0]/2
        f=cv2.resize(fbig,(newx,newy), cv2.cv.CV_INTER_LINEAR);
#	f=fbig
#	cv2.imwrite('ftest.png',f)
#        print 'resized  ', time.clock() 

        hsvimg = cv2.cvtColor(f, cv2.COLOR_RGB2HSV)
        [H,S,V]=cv2.split(hsvimg)
        #print 'split into HSV  ', time.clock()
#	print type(hsvimg)
#	print hsvimg.shape
        cv2.accumulateWeighted(hsvimg,avg1,0.07)
        #print 'Averaged  ', time.clock()

        hsvres1 = cv2.convertScaleAbs(avg1)

        [Havg,Savg,Vavg]=cv2.split(hsvres1)
        #print 'Average split into HSV', time.clock()

        diffmask1=cv2.absdiff(Havg,H)
        diffmask2=cv2.absdiff(Vavg,V)
        diffmask3=cv2.absdiff(Savg,S)
        #print 'diffmasks made  ', time.clock()

        hthresh=int(25.0-(float(np.amin(Havg))*0.22988))
        if hthresh <0:
            hthresh=0
        #print 'threshold found  ', time.clock()

        blurredimg1=cv2.blur(diffmask1,(7,20))
        blurredimg2=cv2.blur(diffmask2,(7,20))
        blurredimg3=cv2.blur(diffmask3,(7,20))
        #print 'blurred  ', time.clrock()
        ret,mask2=cv2.threshold(blurredimg2,30, 255, cv2.THRESH_BINARY) #h=5 blurry h=20 or more crisp

        ret,mask1=cv2.threshold(blurredimg1,hthresh, 255, cv2.THRESH_BINARY) #v=30
        ret,mask3=cv2.threshold(blurredimg3,35, 255, cv2.THRESH_BINARY) #s=35

        #print 'masks made  ', time.clock()
        maska=cv2.add(mask1,mask2)
        mask=cv2.add(maska,mask3)
	maskdisp=cv2.add(maska,mask3)
        #print 'masks added ', time.clock()


        contours2,hyerarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       # print 'contours found  ', time.clock()
     	contour_list=[]
        possibleparts=[]
        targets=[]
        looplen=0
        if len(contours2)> 5:
            looplen=5
        else:
            looplen=len(contours2)
    	for i in range(len(contours2)):
        	x,y,w,h=cv2.boundingRect(contours2[i])
        	area=w*h
        	contour_list.append([area,x,y,w,h])
    	contour_list.sort(reverse=True)
        for i in range(looplen):

       	    contour_list[i][1]=x
            contour_list[i][2]=y
            contour_list[i][3]=w
            contour_list[i][4]=h

            area=h*w
            ratio=float(w)/float(h)
            fwidth=f.shape[1]
            fheight=f.shape[0]
            totalarea=fwidth*fheight
            person_thresh= int(0.075*totalarea)
            part_thresh=int(person_thresh*0.2)

            if ((area >part_thresh)):# and (ratio >0.2) and ratio <0.6):
                possibleparts.append([x,y,w,h])
                if ((area>person_thresh and ratio >0.08 and ratio <1)):
  #                  cv2.rectangle(maskdisp,(x,y),(x+w,y+h),(0,0,255),2)
   #                 cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),6)
                    targets.append(x+(w/2))
#		    print 'x',x,'w',w
            for j in range(len(possibleparts)):
                x1=possibleparts[j][0]
                y1=possibleparts[j][1]
                w1=possibleparts[j][2]
                h1=possibleparts[j][3]

#	    	cv2.rectangle(f,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
                for k in range(len(possibleparts)-1):
                    k=k+1
                    x2=possibleparts[k][0]
                    y2=possibleparts[k][1]
                    w2=possibleparts[k][2]
                    h2=possibleparts[k][3]
                    vert_thresh=int(fheight/5)
                    ho_thresh=int(fwidth/5)
                    if ((abs((y1+h1)-y2) <vert_thresh) or (abs((y2+h2)-y1) <vert_thresh) and (abs(x1-x2)<ho_thresh)):
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
                        if (ratio >0.08 and ratio <1):
 #                           cv2.rectangle(f,(xnew,ynew),(wnew,hnew),(0,155,0),4)  
                            targets.append(xnew+(wnew)/2)
#			    print 'xnew',xnew, 'wnew',wnew
#	print 'targets found',len(targets)
#	if (counter%5==0):
#        imname='t'+str(counter)+'.png'
#	imname2='g'+str(counter)+'.png'
#        cv2.imwrite(imname,maskdisp)
#	cv2.imwrite(imname2,f)
	sorted_targets=[]
	counter=counter+1
        if len(targets)>0:
	    for i in range(len(targets)):
   		 distance=abs(targets[i]-prevtarget)
   		 sorted_targets.append([distance,targets[i]])
	    sorted_targets.sort()
	    target=sorted_targets[0][1]
	    prevtarget=target
	    targ_counter=0           
	    DestroyVictims(target)
	if targ_counter>20:
		targ_counter=0
		Sprinkle()

def Sprinkle():
	Servo0DP.put(195)
	Servo1DP.put(207)

def DestroyVictims(target):
#    target=320/2
#    target=320-target
    if target>320:
	target=320
    print 'target',target
    offset=2 #in ms, to account for the offset between the pin and nozzle
    servo1pos=242-(0.046*target)-offset
    servo1pos=int(round(servo1pos))
    servo0pos=213-(0.046*target)-offset
    servo0pos=int(round(servo0pos))
    if servo1pos > 250:
        servo1pos=250
    if servo1pos < 0:
        servo1pos=0
   # servo1pos=50
    _Servo0DP = servo0pos	
    Servo0DP.put(_Servo0DP)
    _Servo1DP = servo1pos
    Servo1DP.put(_Servo1DP)

def P0():	# Process 0 controlles servo0
#	_Servo0CP = 99		# by making the current position and desired position unequal,-
#	_Servo0DP = 100		# 	we can be sure we know where the servo really is. (or will be soon)
	while True:
	#	if Servo0CP.empty():			# Constantly update Servo0CP in case the main process needs-
	#		Servo0CP.put(_Servo0CP)		# 	to read it
		if not Servo0DP.empty():		# Constantly read read Servo0DP in case the main process-
			_Servo0DP = Servo0DP.get()	#	has updated it
			#print 'servo 0 pos ', _Servo0DP
		#if _Servo0CP < _Servo0DP:					# if Servo0CP less than Servo0DP
			#_Servo0CP += 1						# incriment Servo0CP up by one
			#Servo0CP.put(_Servo0CP)					# move the servo that little bit
			#_Servo0DP=random.randint(50,250)
			ServoBlaster.write('0=' + str(_Servo0DP) + '\n')	#
			ServoBlaster.flush()
#			time.sleep(3)
#			ServoBlaster.write('0=' + str(50) + '\n')
#			ServoBlaster.flush()
			#time.sleep(5)				#
			#if not Servo0CP.empty():				# throw away the old Servo0CP value,-
				#trash = Servo0CP.get()				# 	it's no longer relevent
		# if _Servo0CP > _Servo0DP:					# if Servo0CP greater than Servo0DP
		# 	_Servo0CP -= 1						# incriment Servo0CP down by one
		# 	Servo0CP.put(_Servo0CP)					# move the servo that little bit
		# 	ServoBlaster.write('0=' + str(_Servo0CP) + '\n')	#
		# 	ServoBlaster.flush()					#
		# 	if not Servo0CP.empty():				# throw away the old Servo0CP value,-
		# 		trash = Servo0CP.get()				# 	it's no longer relevent

def P1():	# Process 1 controlles servo 1 using same logic as above
	# _Servo1CP = 99
	# _Servo1DP = 100
	while True:
		# if Servo1CP.empty():
		# 	Servo1CP.put(_Servo1CP)
		if not Servo1DP.empty():
			_Servo1DP = Servo1DP.get()
		# if _Servo1CP < _Servo1DP:
		# 	_Servo1CP += 1
		# 	Servo1CP.put(_Servo1CP)
		#	_Servo1DP=random.randint(50,250)
			ServoBlaster.write('1=' + str(_Servo1DP) + '\n')
			ServoBlaster.flush()
			# if not Servo1CP.empty():
			# 	trash = Servo1CP.get()
		# if _Servo1CP > _Servo1DP:
		# 	_Servo1CP -= 1
		# 	Servo1CP.put(_Servo1CP)
		# 	ServoBlaster.write('1=' + str(_Servo1CP) + '\n')
		# 	ServoBlaster.flush()
		# 	if not Servo1CP.empty():
		# 		trash = Servo1CP.get()

Process(target=P0, args=()).start()	# Start the subprocesses
Process(target=P1, args=()).start()	#


FindVictim()




