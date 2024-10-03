#!/usr/bin/python3

import cv2
import requests
import numpy as np
import rospy
from std_msgs.msg import String




#cam = "http://192.168.117.135:81/stream"
cam = 0 # Use  local webcam.

cap = cv2.VideoCapture(cam)
if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")

while (True):
    # Capture frame-by-frame
    # hsv = cv2.cvtColor(frame, cv2.COLOR_VGA2HSV)
    ret, current_frame = cap.read()
    if type(current_frame) == type(None):
        print("!!! Couldn't read frame!")
        break

    # Display the resulting frame
    cv2.imshow('frame', current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    Quality_Pass = 0
    Quality_Fail = 0
    Total = 0
    w = 0
    b = 0
    global position
    position = 'home'

    imgg = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to convert the image to binary
    ret, binary_image = cv2.threshold(imgg, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours and detect shapes
    for contour in contours:
        # Approximate the contour to a polygon
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)

    if len(approx) != 4:
        position = 'home'
        print('Object Not Detected')
        

    else:

        #imgg = cv2.cvtColor(current_frame, cv2.COLOR_RGB2GRAY)
        imgg1 = imgg.copy()

        (x, y) = imgg.shape

        for i in range(0, x):
          for j in range(0, y):
              if imgg[i, j] < 100:
                 imgg1[i, j] = 0
              else:
                  imgg1[i, j] = 255

        for i in range(0, x):
          for j in range(0, y):
              if imgg1[i, j] == 0:
                  b = b+1
              else:
                  w = w+1

        percent = (b/(w+b))*100

        if 21< percent < 23:
          position = 'correct'
          print('Quality OK')
          Quality_Pass =+1
          Total =+1
        else:
          position = 'wrong'
          print('Quality_Fail')
          Quality_Fail =+1
          Total =+1
    
    
    try:
       
       rospy.init_node('Inspect_result', anonymous=True)

       pub = rospy.Publisher('Inspection_result', String, queue_size=10)
       rate = rospy.Rate(50)
       pub.publish(position)

    except rospy.ROSInterruptException:
       break




# release the capture
cap.release()
cv2.destroyAllWindows()
