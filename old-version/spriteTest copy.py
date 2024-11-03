#img = cv2.imread("Sprites/Bat/BATWAA0-removebg-preview.png",1)
#img = cv2.resize(img, (400, 400))
#img = cv2.resize(img, (0,0), fx=0.7, fy = 0.7)
#img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
#cv2.imshow("Ghost",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
import cv2
import time
from cmu_graphics import *
#import pydirectinput
#import win32api
video = cv2.VideoCapture(0)

def moveScreen():
    currentPos = 0
    working, image = video.read() #working is a bool if a screenshot is successfully captured, and image is ss of camera feed
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    '''
    The whitest GBR (open cv notation because of how it is stored with numpy arrayrs)
    value is (255,255,255) and the darkest is (0,0,0).
    minimum Maximum Location function gives the darkest and brightest color
    and returns the coordinates of them as a tuple on a 640 x 480 external webcam
    '''
    (_, _, _, maxLoc) = cv2.minMaxLoc(image)
    x, y = maxLoc
    if y < 100:
        return currentPos
    elif x <= 210:
        currentPos = -10
    elif 210 < x <= 430:
        currentPos = 0
    elif x > 430:
        currentPos = 10
    else:
        currentPos = 0
    print(currentPos)
    '''
    When there is no key pressed, key is -1
    key & 0xFF default value is 255 and is combined waitkey to check input key when one is pressed
    If it is the ord(q) which is 113, then the camera turns off
    '''
    cv2.circle(image, (x,y), 30,(255, 0, 0) , 5)
    #cv2.line(image, (x, 0), (x, 480), (255, 0, 0), 5)
    cv2.line(image,(210, 0), (210, 480), (0,0,255), 4)
    cv2.line(image,(430, 0), (430, 480), (0,0,255), 4)
    cv2.rectangle(image,(0,0), (640, 100), (0,0,255), -1)

    resize = cv2.resize(image, (213, 160)) 
    cv2.imshow("window",resize) #show image on screen using window name for it to be displayed on and image source
    '''
    When there is no key pressed, key is -1
    key & 0xFF default value is 255 and is combined waitkey to check input key when one is pressed
    If it is the ord(q) which is 113, then the camera turns off
    '''
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"): 
        runLoop = False
        video.release() #stop capturing video
        cv2.destroyAllWindows #remove camera display
    return currentPos

def onAppStart(app):
    app.stepsPerSecond = 30
    app.ghost1 = "Sprites/Ghost/GhostAttack/GSTATKA0-removebg-preview.png"
    app.ghost2 = "Sprites/Ghost/GhostAttack/GSTATKB0-removebg-preview.png"
    app.ghost3 = "Sprites/Ghost/GhostAttack/GSTATKC0-removebg-preview.png"
    app.ghost4 = "Sprites/Ghost/GhostAttack/GSTATKD0-removebg-preview.png"
    app.ghost5 = "Sprites/Ghost/GhostAttack/GSTATKE0-removebg-preview.png"
    app.ghost6 = "Sprites/Ghost/GhostAttack/GSTATKF0-removebg-preview.png"
    app.ghostIndex = 0
    app.dx = 0
    app.cx = 200

def redrawAll(app):
    #ghostList = [app.ghost1, app.ghost2, app.ghost3, app.ghost4, app.ghost5, app.ghost6, app.ghost4]
    #drawImage(ghostList[app.ghostIndex], 200, 200, align = "center")
    drawCircle(app.cx,300, 50, fill="orange")

def onStep(app):
    app.dx = moveScreen()
    app.cx += app.dx
    if app.ghostIndex < 6:
        app.ghostIndex += 1
    else:
        app.ghostIndex = 0

def main():
    runApp()
main()