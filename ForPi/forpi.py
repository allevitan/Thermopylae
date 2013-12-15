import cv2
import numpy as np
import time
import random
from multiprocessing import Process, Queue

ServoBlaster = open('/dev/servoblaster', 'w')  # This is the program we will use to control the servos
Servo0DP = Queue()	# Servo zero desired position, sent by main and read by subprocess
Servo1DP = Queue()	# Servo one desired position, sent by main and read by subprocess

def FindVictim():
    counter=0  
    targ_counter=0  # This keeps track of how many frames it has been since a target was found.
    prevtarget=100  # This variable will keep track of the previous targets position
    fimg=cv2.imread('ftest.png')  # A test image of the right size
    cap = cv2.VideoCapture(-1)    # Initialize communication with the first camera found
    avg1 = np.float32(fimg)       # Initialize variable as the right typle
    while(1): 
        targ_counter=targ_counter+1  # Increment counter
        _,fbig = cap.read()       # Read frame from camera
        f = fbig                  # Initialize f to something of the right type
        newx,newy=fbig.shape[1]/2,fbig.shape[0]/2  # We want to make the image we work with half a big for speed
        f=cv2.resize(fbig,(newx,newy), cv2.cv.CV_INTER_LINEAR)  # Resize the frame 
        hsvimg = cv2.cvtColor(f, cv2.COLOR_RGB2HSV)  # Move into the HSV colorspace
        [H,S,V]=cv2.split(hsvimg)                    # And split into chanels
        cv2.accumulateWeighted(hsvimg,avg1,0.07)     # Add current image to background model
        hsvres1 = cv2.convertScaleAbs(avg1)          # Convert the background from 32bit to 8 bit
        [Havg,Savg,Vavg]=cv2.split(hsvres1)          # Split average into channels
        diffmask1=cv2.absdiff(Havg,H)                # Calculate the differnce between the current frame
        diffmask2=cv2.absdiff(Vavg,V)                # And the background for each channel
        diffmask3=cv2.absdiff(Savg,S)
        hthresh=int(25.0-(float(np.amin(Havg))*0.22988))    # Adjust the threshold for the light conditions
        if hthresh <0:                               # But make sure it is positive
            hthresh=0
        blurredimg1=cv2.blur(diffmask1,(7,20))       # Blurr all the differences.  Blurr vertically more than 
        blurredimg2=cv2.blur(diffmask2,(7,20))       # horizontally.
        blurredimg3=cv2.blur(diffmask3,(7,20))
        ret,mask2=cv2.threshold(blurredimg2,30, 255, cv2.THRESH_BINARY)         # Convert each channel to a biniary (black or white) imgage
        ret,mask1=cv2.threshold(blurredimg1,hthresh, 255, cv2.THRESH_BINARY) 
        ret,mask3=cv2.threshold(blurredimg3,35, 255, cv2.THRESH_BINARY)
        maska=cv2.add(mask1,mask2)                   # Add all the channels together to get a single mask
        mask=cv2.add(maska,mask3)
        #maskdisp=cv2.add(maska,mask3)               # This mask is good for debugging.  the 'mask' image gets modified later
        contours2,hyerarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  #Find all the outer contours of the mask
     	contour_list=[]   # We will put the sorted contours into this list
        possibleparts=[]  # We will put contours that are not big enough to be people, but could be parts of people in this list
        targets=[]        # We will put the X position of people in this list
        looplen=0         # This variable ensure we don't have to take the time to look at every contour
        if len(contours2)> 5:    # We will only care about the 5 biggest contours
            looplen=5
        else:
            looplen=len(contours2)
    	for i in range(len(contours2)):
        	x,y,w,h=cv2.boundingRect(contours2[i])     # Draw a rectangle around each contour
        	area=w*h                                   # And figure out how large this rectangle is 
        	contour_list.append([area,x,y,w,h])        # Add the rectangles and sizes to the list
    	contour_list.sort(reverse=True)                # Sort the list, largest size first
        for i in range(looplen):
       	    contour_list[i][1]=x                       # Unpack the list.  (x,y) is the upper left corner, 
            contour_list[i][2]=y                       # w is the width of the box, and h is the height
            contour_list[i][3]=w
            contour_list[i][4]=h
            area=h*w                                   # figure out the area, and how fat/skinny the box is
            ratio=float(w)/float(h)
            fwidth=f.shape[1]                          # read the height and width of the frame
            fheight=f.shape[0]
            totalarea=fwidth*fheight
            person_thresh= int(0.075*totalarea)        # For a contour to be a possible person, it must be at least yea big
            part_thresh=int(person_thresh*0.2)         # A possible body part must be yea bign

            if ((area >part_thresh)):                  # If the current contour is a possible bodypart, add it to the list
                possibleparts.append([x,y,w,h])
                if ((area>person_thresh and ratio >0.08 and ratio <1)): # If it is big enough and person shaped, it is a person    
                    #cv2.rectangle(f,(x,y),(x+w,y+h),(0,255,0),6)       # This will draw rectangeles around any people on the frame, good for debugging
                    targets.append(x+(w/2))            # Add the center of the rectangles x position to the list of targets
            for j in range(len(possibleparts)):        # This loop handles the case where a person is multiple contours
                x1=possibleparts[j][0]                 # Unpack the list
                y1=possibleparts[j][1]
                w1=possibleparts[j][2]
                h1=possibleparts[j][3]

#	    	    cv2.rectangle(f,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)  # More rectanges can be drawn for debugging
                for k in range(len(possibleparts)-1):  # We have to loops to join any two contours together
                    k=k+1                              # Re-adjust the index
                    x2=possibleparts[k][0]             # And unpack
                    y2=possibleparts[k][1]
                    w2=possibleparts[k][2]
                    h2=possibleparts[k][3]
                    vert_thresh=int(fheight/5)         # These thresholds set how far away two contours can be 
                    ho_thresh=int(fwidth/5)            # In the vertical and horizontal directions and still be considered one object
                    if ((abs((y1+h1)-y2) <vert_thresh) or (abs((y2+h2)-y1) <vert_thresh) and (abs(x1-x2)<ho_thresh)): # If the conditions are met
                        if x1 > x2:     #Find the x,y,w, and h for the box that will enclose both smaller boxes
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

                        ratio=abs(float(xnew-wnew)/float(ynew-hnew))    # Determine the shape of this new box
                        if (ratio >0.08 and ratio <1):                  # If the box is person shaped
 #                           cv2.rectangle(f,(xnew,ynew),(wnew,hnew),(0,155,0),4)  #Another rectangle for debugging  
                            targets.append(xnew+(wnew)/2)               # Add the x coordinate of the center to the target list
#   imname='t'+str(counter)+'.png'        # These commands can create an image of each frame/mask for debugging
#	imname2='g'+str(counter)+'.png'
#   cv2.imwrite(imname,maskdisp)
#	cv2.imwrite(imname2,f)
	sorted_targets=[]          # We will now figure out which target requires the least moving
	counter=counter+1
        if len(targets)>0:     # If there are targets
            for i in range(len(targets)):
                distance=abs(targets[i]-prevtarget) # Figure out how far away each target is from the last target
                sorted_targets.append([distance,targets[i]]) 
            sorted_targets.sort() #Sort by this distance
            target=sorted_targets[0][1] #Select the closest target
            prevtarget=target
            targ_counter=0              # Reset this counter         
	        DestroyVictims(target)      # Call the function to toalk to the servos
	if targ_counter>20:                 # If it has been a while since a target was found
		targ_counter=0
		Sprinkle()                      # Send the sprinkler back to normal sprinling mode

def Sprinkle():
	Servo0DP.put(163)                   # This corresponds to the open, 180deg normal sprinkle range
	Servo1DP.put(292)                   # The numbers are the pulse width in ms we will send to the servos

def DestroyVictims(target):
    offset=6                            #in ms, this helps us tune the range of the servos
    minrange=2                          # This ensures there is space for the mechanical trigger between the two servo arms
    servo1pos=169-(0.075*target)-offset+minrange    #This is a linear function we found to map target position to pulse ms
    servo1pos=int(round(servo1pos))                 #We can only have whole number ms
    servo0pos=163-(0.075*target-offset-minrange
    servo0pos=int(round(servo0pos))
    Servo0DP.put(servo0pos)             # Put these values in their respective queues
    Servo1DP.put(servo1pos)

def P0():	# Process 0 controlles servo0
	while True:
		if not Servo0DP.empty():		# Constantly read read Servo0DP in case the main process-
			_Servo0DP = Servo0DP.get()	#	has updated it
			ServoBlaster.write('0=' + str(_Servo0DP) + '\n')	#Write any new value to the servo
			ServoBlaster.flush()                        #Clear it
def P1():	# Process 1 controlles servo 1 using same logic as above
	while True:
		if not Servo1DP.empty():
			_Servo1DP = Servo1DP.get()
			ServoBlaster.write('1=' + str(_Servo1DP) + '\n')

Process(target=P0, args=()).start()	# Start the subprocess for servo 0
Process(target=P1, args=()).start()	# Start the subprocess for servo 1


FindVictim() # call the main function




