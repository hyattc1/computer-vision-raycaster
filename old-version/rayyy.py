from cmu_graphics import *
import math
import random
import numpy as np

def onAppStart(app):

    app.width = 600
    app.height = 500
   
    app.map = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
           
    app.blockWidth = app.width/ len(app.map[0])
    app.blockHeight = app.height/ len(app.map)
   
    app.px = 200
    app.py = 200
    app.pAngle = 0
   
    app.pSpeed = 4
    app.posX = 200
    app.posY = 200
    app.dx = 0
    app.dy = 0
   
    app.a = 0
    app.b = 0
    app.c = 0
   
    app.currentKey = ''
    app.mx = 0
    app.my = 0
    app.quad = 1
   
    app.numOfRays = 40
    app.FOV = math.pi/3
    app.rayList = [[1, 1, 1, 1]]*app.numOfRays

    app.dof = 3
   
    app.wallX = 0
    app.Rcollide = -1
    app.Ccollide = -1
   
    app.lA = 0
    app.lB = 0
   
    app.tempDX = 0
    app.tempDY = 0
    app.rx = 0
    app.ry = 0
   
    app.switchLegLogic = False
    app.tempLegB = 0
    app.heldKey = None
    app.yaw = 0
    app.counter = 0
   
    app.monsterR = 7
    app.monsterC = 3
    app.monsterCounter = 0
    app.pathList = []
   
    app.shoot = False


   
#==================================================
#           redrawALL
#==================================================

def redrawAll(app):
    #draw2Dboard(app, 100)
    #drawPlayer(app)
    #drawRayCastLines(app)
    #drawMonster(app)
   
    #drawRayLines(app)
    #drawDebugLines(app)
    #drawDegubInfo(app)
   
    draw3DMap(app)
    #ghostW, ghostH = getImageSize(app.ghost)
    #drawImage(app.ghost, app.spriteX, app.spriteY, width = ghostW * 0.8, height = ghostH * 0.8, align = "bottom")

#==================================================
#           Draw Ray Lines
#==================================================

def drawRayCastLines(app):
    for ray in range(app.numOfRays):
        drawLine(app.posX, app.posY, app.rayList[ray][1], app.rayList[ray][3], fill = 'yellow', lineWidth = 1)


#==================================================
#           Draw Board
#==================================================    

def draw2Dboard(app, opacity):
    rows, cols = len(app.map), len(app.map[0])
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = opacity)
    for row in range(rows):
        for col in range(cols):
            if(app.map[row][col] == 1):
                if(row == app.Rcollide and col == app.Ccollide):
                    #drawRect(col*app.blockWidth, row*app.blockHeight, app.blockWidth, app.blockHeight, fill = 'red', border = 'White')
                    #drawLabel(f'({row}, {col})', col*app.blockWidth+app.blockWidth/2, row*app.blockHeight+app.blockHeight/2, size = 20)
                    pass
                else:
                    drawRect(col*app.blockWidth, row*app.blockHeight, app.blockWidth, app.blockHeight, fill = None, border = 'White', opacity = opacity)
            else:
                drawRect(col*app.blockWidth, row*app.blockHeight, app.blockWidth, app.blockHeight, fill = None, border = 'yellow', borderWidth = .2, opacity = opacity)
               
#==================================================
#           draw3DMap
#==================================================

def draw3DMap(app):
    grad = gradient('red', 'orange', start = 'top')
   
    drawRect(0, 0, app.width, app.height/1.5, fill = 'black')
    #if(app.pAngle < math.pi):
        #drawCircle(app.width - app.width*app.pAngle*.75, 150, 100, fill = 'yellow', opacity = 100)
       
    for ray in range(len(app.rayList)):
        dist = distance(app.rayList[ray][0], app.rayList[ray][1], app.rayList[ray][2], app.rayList[ray][3])*.02
        quad = getQuad(app.pAngle)
       
        scale = app.width//app.numOfRays
        FOV = math.pi/3
        screenDist = (app.width/2)/math.tan(FOV/2)
        projectionHeight = (screenDist/(dist+.001))*1.3
   
        if(0 <= projectionHeight <= 255*2):
            color = rgb(projectionHeight/2, projectionHeight/2, projectionHeight/2)
        else:
            color = 'white'
        floorColor = gradient('gray', 'white', start = 'top')
        floorColor = 'gray'
       
        drawRect(ray*scale, (app.height/2 - abs(projectionHeight//2))+app.yaw, scale, abs(projectionHeight), fill = color)
        drawRect(ray*scale, (app.height/2 - abs(projectionHeight//2))+abs(projectionHeight)+app.yaw, scale, projectionHeight*5, fill = floorColor)
       
    drawRect(app.width/2, app.height-150, 30, 80)    
   
    drawCrosshare(app)
    drawInfoBar(app)
    if(app.shoot):
        randX = random.randint(app.width/2-25, app.width/2+25)
        randY = random.randint(app.height/2-25, app.height/2+25)
        drawCircle(randX, randY, 5, fill = 'white')

def drawInfoBar(app):
    drawRect(0, app.height-65, app.width, 65, fill = 'white', border = 'black')
    drawRect(20, app.height-50, 100, 40, fill = 'yellow', border = 'black')
    drawLabel('Health: 100', 71, app.height-30, fill = 'red', size = 15, bold = True)

def drawCrosshare(app):
    drawCircle(app.width/2, app.height/2, 15, fill = None, border = 'black', opacity = 50, borderWidth = 2)
    drawCircle(app.width/2, app.height/2, 30, fill = None, border = 'black', opacity = 50, borderWidth = 4)
    drawRect(app.width/2-40, app.height/2-2.5, 30, 5, fill = 'red', opacity = 50)
    drawRect(app.width/2+10, app.height/2-2.5, 30, 5, fill = 'red', opacity = 50)
   
    drawRect(app.width/2-2.5, app.height/2-40, 5, 30, fill = 'red', opacity = 50)
    drawRect(app.width/2-2.5, app.height/2+10, 5, 30, fill = 'red', opacity = 50)
   
   
#==================================================
#           Draw Player
#==================================================

def drawPlayer(app):
    drawCircle(app.posX, app.posY, 3, fill = 'white', border = 'black')
    drawLabel(f'{app.posX//app.blockWidth}, {app.posY//app.blockHeight}', app.posX, app.posY, fill = 'cyan')
    drawLabel(f'{app.posX//app.blockWidth}, {app.posY//app.blockHeight}', app.posX, app.posY, fill = 'cyan')

#==================================================
#           Raycasting
#==================================================

def raycast(app):
    dof = app.dof
    counter = 0
    tempAngle = app.pAngle - .5
    for ray in range(app.numOfRays):
       
        density = math.pi/(4*app.numOfRays)
        dof = app.dof+200
        ry = app.posY
        rx = app.posX
        tempAngle += density
        while (dof > 0):
            quad = getQuad(tempAngle)
            if(not app.switchLegLogic):
                legA = distance(app.posX, app.posX, ry, app.posY)
                if(tempAngle > math.pi):
                    ry += 10
                    legB = legA*math.tan(math.pi/2+tempAngle)
                elif(tempAngle < math.pi):
                    ry -= 10
                    legB = legA*math.tan(math.pi/2-tempAngle)
                rx = legB + app.posX    
            else:
                legB = distance(rx, app.posX, app.posY, app.posY)
                if(app.pAngle >= 7*math.pi/4 or app.pAngle <= math.pi/4):
                    rx += 10
                    legA = legB*math.tan(tempAngle)*-1
                    ry = legA + app.posY
                elif(3*math.pi/4 <= app.pAngle <=  5*math.pi/4):
                    rx -= 10
                    legA = legB*math.tan(tempAngle)
                    ry = legA + app.posY
           
            app.rx = rx
            app.ry = ry
            lineTrace = [app.posX, rx, app.posY, ry]
           
            if(rayCollision(app, lineTrace)[0] or outOfRange(ry, rx, app, 10)):
                app.lA = rounded(abs(legA))
                app.lB = rounded(abs(legB))
                app.rayList[ray] = lineTrace  
                break
            dof -= 1
   
#==================================================
#           Player Collision
#==================================================

def playerCollision(app):
    rad = 0
    rows = len(app.map)
    cols = len(app.map[0])
    for r in range(rows):
        for c in range(cols):
            if(app.map[r][c] == 1):
                if(c*app.blockWidth-rad <= app.posX <= c*app.blockWidth + app.blockWidth+rad and r*app.blockHeight-rad <= app.posY <= r*app.blockHeight+app.blockHeight+rad):
                    app.posX -= app.tempDX/3
                    app.posY -= app.tempDY/3
                    return True
    return False

#==================================================
#           Ray out of range
#==================================================

def outOfRange(ry, rx, app, rayRange):
    if(ry > app.posY + rayRange*app.blockHeight):
        return True
    elif(rx > app.posX + rayRange*app.blockWidth):
        return True
    elif(ry < app.posY - rayRange*app.blockHeight):
        return True
    elif(rx < app.posX - rayRange*app.blockWidth):
        return True
    return False
   
#==================================================
#           Get Quad
#==================================================

def getQuad(angle):
    if(0 <= angle <= math.pi/2):
        return 1
    if(math.pi/2 <= angle <= math.pi):
        return 2
    if(math.pi <= angle <= 3*math.pi/2):
        return 3
    elif(3*math.pi/2 <= angle <= 2*math.pi):
        return 4
#==================================================
#           Ray Collision
#==================================================

def rayCollision(app, L):
    rows = len(app.map)
    cols = len(app.map[0])
   
    for r in range(rows):
        for c in range(cols):
            if(app.map[r][c] == 1):
                if(c*app.blockWidth <= L[1] <= c*app.blockWidth + app.blockWidth and r*app.blockHeight <= L[3] <= r*app.blockHeight+app.blockHeight):
                    app.Rcollide = r
                    app.Ccollide = c
                    return [True, r*app.blockHeight, c*app.blockWidth]
    return [False]
   
#==================================================
#           Player Movement
#==================================================
     
def playerMovement(app):
    app.dx = 0
    app.dy = 0
    if not playerCollision(app):
        if(app.currentKey == 'a'):
            app.dx = app.pSpeed*math.cos(app.pAngle)
            app.dy = app.pSpeed*math.sin(app.pAngle)
        elif(app.currentKey == 'w'):
            app.dx = app.pSpeed*math.cos(app.pAngle)
            app.dy = app.pSpeed*math.sin(app.pAngle)*-1
        elif(app.currentKey == 'd'):
            app.dx = app.pSpeed*math.cos(app.pAngle)*-1
            app.dy = app.pSpeed*math.sin(app.pAngle)*-1
        elif(app.currentKey == 's'):
            app.dx = app.pSpeed*math.cos(app.pAngle)*-1
            app.dy = app.pSpeed*math.sin(app.pAngle)
        #app.yaw = 5*math.sin(app.counter)
        if(app.dx != 0):
            app.tempDX = app.dx
        if(app.dy != 0):
            app.tempDY = app.dy
   

#==================================================
#           get Angle
#==================================================

def getAngle(app):
    if(app.currentKey == 'right'):
        app.pAngle += .05
    elif(app.currentKey == 'left'):
        app.pAngle -= .05
    elif(app.currentKey == 'up'):
        app.yaw += 10
    elif(app.currentKey == 'down'):
        app.yaw -= 10
   
    app.pAngle = app.pAngle % 6.24
   
def oldGetAngle(app):
    a = distance(app.mx, app.mx, app.my, app.posY)+.00001
    b = distance(app.mx, app.posX, app.posY, app.posY)+.00001
   
    app.a = a
    app.b = b
    app.c = distance(app.mx, app.posX, app.my, app.posY)
   
    if(app.my > app.posY and app.mx > app.posX):
        app.quad = 4
    elif(app.my > app.posY and app.mx < app.posX):
        app.quad = 3
    elif(app.my < app.posY and app.mx < app.posX):
        app.quad = 2
    else:
        app.quad = 1
       
    quadAdd = math.pi/2 * (app.quad-1)
   
    if(app.quad % 2 == 1):
        app.pAngle = pythonRound(math.atan(a/b) + quadAdd , 2)
    else:
        app.pAngle = pythonRound(math.atan(b/a) + quadAdd , 2)
       
       
#==================================================
#           on Key Press
#==================================================

def onKeyPress(app, key):
    if(key == 'space'):
        app.shoot = True
    app.currentKey = key

def onKeyRelease(app, key):
    app.currentKey = None
   
#==================================================
#           on Key Release
#==================================================

def onKeyRelease(app, key):
    app.dx = 0
    app.dy = 0
    app.currentKey = ''

def switchLegLogic(app):
    if((2*math.pi >= app.pAngle >= 7*math.pi/4) or (0 <= app.pAngle <= math.pi/4) or (3*math.pi/4 <= app.pAngle <=  5*math.pi/4) ):
        app.switchLegLogic = True
    else:
        app.switchLegLogic = False
       
#==================================================
#           on Step
#==================================================

def onStep(app):
    app.counter += .2    
    getAngle(app)
    playerMovement(app)
    raycast(app)
    switchLegLogic(app)
   
   
    app.posX += app.dx
    app.posY += app.dy
   
def onMouseMove(app, mx, my):
    #app.mx = mx
    #app.my = my
    app.c = distance(mx, app.posX, my, app.posY)
    app.spriteX = mx
    app.spriteY = my


def distance(x0, x1, y0, y1):
    return ((x0-x1)**2+(y0-y1)**2)**.5
   
def main():
    runApp()

main()