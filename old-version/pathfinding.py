from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from cmu_graphics import *
import math
import os 
import pathlib

m = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
#m = [ [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0],[0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0],[0, 1, 0, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]

class Enemy:
    def __init__(self,row,col, sprite):
        self.row = row
        self.col = col
        self.sprite = sprite
        self.speed = 10

class Player:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.speed = 1

def onAppStart(app):
    app.matrix = m #replace with level needed for maze
    #app.soundDic = {}
    #loadSounds(app)
    setBoard(app) #replace this (sets board)
    app.path = None
    setChars(app)
    app.stepsPerSecond = app.enemy.speed #have relation between enemy speed and steps as steps indicate how fast the enemy moves
    app.steps = 0 #for onStep
    app.radius = 10 #for circles, may not be needed
    app.lastPath = None
    setEnemyPath(app)

def setBoard(app):
    app.rows = len(app.matrix)
    app.cols = len(app.matrix[0])
    app.boardLeft = 50
    app.boardTop = 50
    app.boardWidth = 500
    app.boardHeight = 500
    app.height = 600
    app.width = 600
    app.gameOver = False

def loadSound(relativePath):
    pass
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    #absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    #url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    #return Sound(url)

#imports sound library into a dictionary
def loadSounds(app):
    pass
    #app.soundDic['footsteps'] = loadSound("FOOTSTEPS SOUND EFFECT (HD)-[AudioTrimmer.com].mp3")
    #app.soundDic['enemyClose'] = {0: loadSound("Ghost 100 (mp3cut.net).mp3") , 1: loadSound("Bat Sound Passive.mp3"), 2: loadSound("Zombie.mp3")}
    #app.soundDic['deathSound'] = {0: loadSound("Ghost Sound Effects-[AudioTrimmer.com].mp3"), 1: loadSound("Bat Death.mp3"), 2: loadSound("Zombie Death (Minecraft Sound) - Sound Effect for editing-[AudioTrimmer.com].mp3")}
    #app.soundDic['playerDamage'] =  loadSound("Minecraft Damage (Oof) - Sound Effect (HD)-[AudioTrimmer.com].mp3")


def setChars(app):
    width, height = getCellSize(app)
    app.player = Player(27,25) #sets player's starting position based on row and column
    app.player.pixelX, app.player.pixelY = getCellLeftTop(app, app.player.row, app.player.col)
    app.player.pixelX += width //2
    app.player.pixelY += height //2
    app.enemy = Enemy(28,17,2) #same as player, but adds third input for type of enemy
    app.enemy.pixelX, app.enemy.pixelY = getCellLeftTop(app, app.enemy.row, app.enemy.col)
    app.enemy.pixelX += width //2
    app.enemy.pixelY += height //2

#from library, sets a grid with the matrix in onAppStart and then finds a path
def setEnemyPath(app):
    grid = Grid(matrix=app.matrix)
    start = grid.node(app.enemy.col, app.enemy.row)
    end = grid.node(app.player.col, app.player.row)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    app.path = path

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            #left, top = getCellLeftTop(app, row, col)
            #drawLabel(f'{row},{col}', left + 10,top + 10)
            if (app.matrix[row][col] == 0):
                drawCell(app, row, col)

def getCell(app, x, y):
    dx = x - app.boardLeft
    dy = y - app.boardTop
    cellWidth, cellHeight = getCellSize(app)
    row = math.floor(dy / cellHeight)
    col = math.floor(dx / cellWidth)
    if (0 <= row < app.rows) and (0 <= col < app.cols):
      return (row, col)
    else:
      return None

def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=None, border='black')

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def redrawAll(app):
    drawBoard(app)
    if app.gameOver:
        drawGameOver(app)
    else:
        drawPlayer(app)
        drawEnemy(app)

def drawGameOver(app):
    drawLabel('TEST',app.width // 2, app.height // 2, fill = 'red', size = 16)

def drawPlayer(app):
    drawCircle(app.player.pixelX, app.player.pixelY, app.radius, fill='blue')

def drawEnemy(app):
    drawCircle(app.enemy.pixelX, app.enemy.pixelY, app.radius, fill = 'red')


def onKeyPress(app, key):
    if key == 'up':
        movePlayer(app,-1,0)
    elif key == 'down':
        movePlayer(app,1,0)
    elif key == 'left':
        movePlayer(app,0,-1)
    elif key == 'right':
        movePlayer(app,0,1)
    

def onKeyHold(app, key):
    if 'up' in key:
        movePlayer(app,-1,0)
    elif 'down' in key:
        movePlayer(app,1,0)
    elif 'left' in key:
        movePlayer(app,0,-1)
    elif 'right' in key:
        movePlayer(app,0,1)
    #app.soundDic['footsteps'].play()

def movePlayer(app,drow,dcol):
    #change stepsPerSecond to speed wanted
    app.player.pixelX += dcol * app.stepsPerSecond
    app.player.pixelY += drow * app.stepsPerSecond
    app.player.row, app.player.col = getCell(app, app.player.pixelX, app.player.pixelY)
    if(app.matrix[app.player.row][app.player.col] == 0):
        app.player.pixelX -= dcol * app.stepsPerSecond
        app.player.pixelY -= drow * app.stepsPerSecond
        app.player.row, app.player.col = getCell(app, app.player.pixelX, app.player.pixelY) 

def moveEnemy(app,drow,dcol):
    app.enemy.pixelX += dcol * app.stepsPerSecond
    app.enemy.pixelY += drow * app.stepsPerSecond
    

def checkSound(app):
    if(distance(app.enemy.pixelX,app.enemy.pixelY,app.player.pixelX,app.player.pixelY) < 100):
        pass
        #app.soundDic['enemyClose'][app.enemy.sprite].play()
    playerCell = getCell(app,app.player.pixelX,app.player.pixelY)
    enemyCell = getCell(app,app.enemy.pixelX,app.enemy.pixelY)
    if (playerCell == enemyCell):
        pass
        #app.soundDic['playerDamage'].play()


def getDir(app):
    if(len(app.path) < 1 or    app.path == None):
        return 0,0
    elif(app.lastPath == None):
        x0, y0 = app.enemy.row, app.enemy.col
        x1, y1 = app.path[1]
    else:
        x0, y0 = app.lastPath
        x1, y1 = app.path[0]
    dx, dy = x1 - x0, y1 - y0
    return dx, dy

def convertToPixel(app,t):
    r,c = t
    left, top = getCellLeftTop(app, r, c)
    width, height = getCellSize(app)
    return (width / 2 + left, height / 2 + top)

def onStep(app):
    app.steps += 1
    checkSound(app)
    if not app.gameOver:
        enemyPlacement(app)

def enemyPlacement(app):
    targetX, targetY = convertToPixel(app,(app.enemy.row, app.enemy.col)) #target next Cell
    dx, dy = getDir(app)
    if(len(app.path) == 1):
        setEnemyPath(app)
    if ((abs(app.enemy.pixelX - targetX) < 10) and dx != 0) or (dy != 0 and (abs(app.enemy.pixelY - targetY) < 10)) or (dx == 0 and dy == 0):
        app.lastPath = app.path.pop(0)
        if(len(app.path) < 1):
            setEnemyPath(app)
        else:
            col, row = app.path[0]
            app.enemy.row = row
            app.enemy.col = col
            setEnemyPath(app)
    else:
        moveEnemy(app,dy,dx)
    if app.steps % 3 == 0:
        setEnemyPath(app)
    

runApp()