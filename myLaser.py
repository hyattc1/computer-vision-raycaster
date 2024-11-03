import cv2
import numpy as np
#import pydirectinput
#import win32api


video = cv2.VideoCapture(1)
currnetPos = 0
enterLoopCounter = 0
runLoop = True
while runLoop:
    #enterLoopCounter += 1
    #if enterLoopCounter % 1000 != 0: #slow the framerate to let game run faster
    #    continue
    working, image = video.read() #working is a bool if a screenshot is successfully captured, and image is ss of camera feed
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    '''
    The whitest GBR (open cv notation because of how it is stored with numpy arrayrs)
    value is (255,255,255) and the darkest is (0,0,0).
    minimum Maximum Location function gives the darkest and brightest color
    and returns the coordinates of them as a tuple on a 640 x 480 external webcam
    '''
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(image)
    x, y = maxLoc
    if x <= 210:
        currentPos = -1
    elif 210 < x <= 430:
        currentPos = 0
    elif x > 430:
        currentPos = 1
    else:
        currentPos = 0
    print(currentPos)
    key = cv2.waitKey(1)
    image = cv2.circle(image, (x,y), 30,(255, 0, 0) , 5)
    cv2.imshow("window",image) #show image on screen using window name for it to be displayed on and image source
    '''
    When there is no key pressed, key is -1
    key & 0xFF default value is 255 and is combined waitkey to check input key when one is pressed
    If it is the ord(q) which is 113, then the camera turns off
    '''
    if key & 0xFF == ord("q"): 
        runLoop = False
        video.release() #stop capturing video
        cv2.destroyAllWindows #remove camera display
exit() #close code to prevent infinite loop