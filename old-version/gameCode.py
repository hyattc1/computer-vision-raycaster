from cmu_graphics import *
import math
import os
import pathlib
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import cv2

m = [0,0,0]
m[0] = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0]]
#m = [ [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0],[0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 1, 0],[0, 1, 0, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]]

m[1] = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]]

def onAppStart(app):
    app.width = 600
    app.height = 500
    app.difficulty = ['Easy', 'Medium', 'Hard']
    app.diffIndex = 0
    app.fov = math.pi
    app.paused = False
    app.health = 100
    app.weapon = Wrench(Weapon)
    app.victory = False
    app.defeat = False
    app.startTime = 0
    app.damaged = False
    app.steps = 0 #for onStep
    app.radius = 10 #for circles, may not be needed
    app.lastPath = None
    app.key = False
    app.index = 0 
    app.matrix = m #replace with level needed for maze
    setBoard(app) #replace this (sets board)
    app.keyC = None
    setChars(app)
    app.angle = 0
    app.grid = None
    app.hit = False
    app.hitTimer = 0
    app.attackTimer = 0
    setEnemyPath(app,app.index)

    app.path = None
    app.attackRange = False
    app.attack = False

    #logo
    app.inStartWidth = False
    app.logoIncreasing = True
    app.logoTimer = 0
    app.logoScale = 0.7
    app.logo = "Images/WeanAfterDarkLogo.png"

    app.startBackground = "Images/weanBackground.jpg"
    #Scotty
    app.scottyTimer = 0
    app.scottyCx = 470
    app.scottyIndex = 0
    app.scotty1 = "Sprites/Scottie/scottie1-removebg-preview.png"
    app.scotty2 = "Sprites/Scottie/scottie2-removebg-preview.png"
    app.scotty3 = "Sprites/Scottie/scottie3-removebg-preview.png"
    app.scotty4 = "Sprites/Scottie/scotty4-removebg-preview.png"
    app.scotty5 = "Sprites/Scottie/scotty5-removebg-preview.png"
    app.scotty6 = "Sprites/Scottie/scotty6-removebg-preview.png"
    app.scotty7 = "Sprites/Scottie/scotty7-removebg-preview.png"
    app.scotty8 = "Sprites/Scottie/scotty8-removebg-preview.png"

    app.weanCube = "Images/wean hall.jpg"

    ############### Settings
    app.settingsText = "Images/SettingsText.png"
    ############### How to Play
    app.howToPlayText = "Images/HowToPlay.png"
    ##############play
    app.wrenchLogo = "Sprites/Wrench/wrench0.png"
    app.plasmaLogo = "Sprites/PlasmaBlaster/plasma0.png"


    ################################ MAPS
    app.map1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0]]
               
    app.map2  = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]]
               
    app.map3 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0],#Key location
                [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                [0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
                [0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,0],
                [0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]]

    #####################################################################################
    #Sprites & Stuff
    #####################################################################################
    #weapon 0: Wrench (starter)
    app.swinging = False
    app.wrenchTimer = 0
    app.wrenchIndex = 0
    app.wrench1 = "Sprites/Wrench/wrench1-removebg-preview.png"
    app.wrench2 = "Sprites/Wrench/wrench2-removebg-preview.png"
    app.wrench3 = "Sprites/Wrench/wrench3-removebg-preview.png"
    app.wrench4 = "Sprites/Wrench/wrench4-removebg-preview.png"
    app.wrench5 = "Sprites/Wrench/wrench5-removebg-preview.png"
    app.wrench6 = "Sprites/Wrench/wrench6-removebg-preview.png"
    app.wrench7 = "Sprites/Wrench/wrench7-removebg-preview.png"
    app.wrench8 = "Sprites/Wrench/wrench8-removebg-preview.png"
    app.wrench9 = "Sprites/Wrench/wrench9-removebg-preview.png"
    app.wrench10 = "Sprites/Wrench/wrench10-removebg-preview.png"
    app.wrench11 = "Sprites/Wrench/wrench11-removebg-preview.png"
    app.wrench12 = "Sprites/Wrench/wrench12-removebg-preview.png"
    app.wrench13 = "Sprites/Wrench/wrench13-removebg-preview.png"
    app.wrench14 = "Sprites/Wrench/wrench14-removebg-preview.png"
    app.wrench15 = "Sprites/Wrench/wrench15-removebg-preview.png"
    app.wrench16 = "Sprites/Wrench/wrench16-removebg-preview.png"
    app.wrench17 = "Sprites/Wrench/wrench17-removebg-preview.png"

    #weapon 1: Plasma Blaster
    app.shooting = False
    app.plasmaTimer = 0
    app.plasmaIndex = 0
    app.plasma1 = "Sprites/PlasmaBlaster/plasma1-removebg-preview.png"
    app.plasma2 = "Sprites/PlasmaBlaster/plasma2-removebg-preview.png"
    app.plasma3 = "Sprites/PlasmaBlaster/plasma3-removebg-preview.png"
    app.plasma4 = "Sprites/PlasmaBlaster/plasma4-removebg-preview.png"
    app.plasma5 = "Sprites/PlasmaBlaster/plasma5-removebg-preview.png"
    app.plasma6 = "Sprites/PlasmaBlaster/plasma6-removebg-preview.png"
    app.plasma7 = "Sprites/PlasmaBlaster/plasma7-removebg-preview.png"
    app.plasma8 = "Sprites/PlasmaBlaster/plasma8-removebg-preview.png"
    app.plasma9 = "Sprites/PlasmaBlaster/plasma9-removebg-preview.png"
    app.plasma10 = "Sprites/PlasmaBlaster/plasma10-removebg-preview.png"
    app.plasma11 = "Sprites/PlasmaBlaster/plasma11-removebg-preview.png"
    app.plasma12 = "Sprites/PlasmaBlaster/plasma12-removebg-preview.png"
    app.plasma13 = "Sprites/PlasmaBlaster/plasma13-removebg-preview.png"
    app.plasma14 = "Sprites/PlasmaBlaster/plasma14-removebg-preview.png"
    app.plasma15 = "Sprites/PlasmaBlaster/plasma15-removebg-preview.png"
    app.plasma16 = "Sprites/PlasmaBlaster/plasma16-removebg-preview.png"
    app.plasma17 = "Sprites/PlasmaBlaster/plasma17-removebg-preview.png"
    app.plasma18 = "Sprites/PlasmaBlaster/plasma18-removebg-preview.png"
    app.plasma19 = "Sprites/PlasmaBlaster/plasma19-removebg-preview.png"
    app.plasma20 = "Sprites/PlasmaBlaster/plasma20-removebg-preview.png"
    app.plasma21 = "Sprites/PlasmaBlaster/plasma21-removebg-preview.png"
    app.plasma22 = "Sprites/PlasmaBlaster/plasma22-removebg-preview.png"
    app.plasma23 = "Sprites/PlasmaBlaster/plasma23-removebg-preview.png"
    app.plasma24 = "Sprites/PlasmaBlaster/plasma24-removebg-preview.png"
    app.plasma25 = "Sprites/PlasmaBlaster/plasma25-removebg-preview.png"
    app.plasma26 = "Sprites/PlasmaBlaster/plasma26-removebg-preview.png"
    app.plasma27 = "Sprites/PlasmaBlaster/plasma27-removebg-preview.png"
    app.plasma28 = "Sprites/PlasmaBlaster/plasma28-removebg-preview.png"
    app.plasma29 = "Sprites/PlasmaBlaster/plasma29-removebg-preview.png"

    ######################################### Ghost Sprite
    app.ghostOnScreen = False
    app.ghostMoving = False
    app.ghostAttacking = False
    app.ghostDying = False
    #Ghost Move
    app.ghostMoveTimer = 0
    app.ghostMoveIndex = 0
    app.ghostMove1 = "Sprites/Ghost/GhostMove/GSTFLYA0-removebg-preview.png"
    app.ghostMove2 = "Sprites/Ghost/GhostMove/GSTFLYB0-removebg-preview.png"
    app.ghostMove3 = "Sprites/Ghost/GhostMove/GSTFLYC0-removebg-preview.png"
    app.ghostMove4 = "Sprites/Ghost/GhostMove/GSTFLYD0-removebg-preview.png"
    app.ghostMove5 = "Sprites/Ghost/GhostMove/GSTFLYE0-removebg-preview.png"
    app.ghostMove6 = "Sprites/Ghost/GhostMove/GSTFLYF0-removebg-preview.png"

    #Ghost Attack
    app.ghostAttackTimer = 0
    app.ghostAttackIndex = 0
    app.ghostAttack1 = "Sprites/Ghost/GhostAttack/GSTATKA0-removebg-preview.png"
    app.ghostAttack2 = "Sprites/Ghost/GhostAttack/GSTATKB0-removebg-preview.png"
    app.ghostAttack3 = "Sprites/Ghost/GhostAttack/GSTATKC0-removebg-preview.png"
    app.ghostAttack4 = "Sprites/Ghost/GhostAttack/GSTATKD0-removebg-preview.png"
    app.ghostAttack5 = "Sprites/Ghost/GhostAttack/GSTATKE0-removebg-preview.png"
    app.ghostAttack6 = "Sprites/Ghost/GhostAttack/GSTATKF0-removebg-preview.png"

    #Ghost Die
    app.ghostDieTimer = 0
    app.ghostDieIndex = 0
    app.ghostDie1 = "Sprites/Ghost/GhostDie/GSTDIEA0-removebg-preview.png"
    app.ghostDie2 = "Sprites/Ghost/GhostDie/GSTDIEB0-removebg-preview.png"
    app.ghostDie3 = "Sprites/Ghost/GhostDie/GSTDIEC0-removebg-preview.png"
    app.ghostDie4 = "Sprites/Ghost/GhostDie/GSTDIED0-removebg-preview.png"
    app.ghostDie5 = "Sprites/Ghost/GhostDie/GSTDIEE0-removebg-preview.png"
    app.ghostDie6 = "Sprites/Ghost/GhostDie/Gstdief0-removebg-preview.png"

    ########################################## Bat Sprite
    app.batOnScreen = False
    app.batMoving = False
    app.batDying = False
    #Bat Move (there is no bat attack sprite, when it is near it keeps flapping and damaging player)
    app.batMoveTimer = 0
    app.batMoveIndex = 0
    app.batMove1 = "Sprites/Bat/BatMove/BATWAA0-removebg-preview.png"
    app.batMove2 = "Sprites/Bat/BatMove/BATWAB0-removebg-preview.png"
    app.batMove3 = "Sprites/Bat/BatMove/BATWAC0-removebg-preview.png"
    app.batMove4 = "Sprites/Bat/BatMove/BATWAD0-removebg-preview.png"
    app.batMove5 = "Sprites/Bat/BatMove/BATWAE0-removebg-preview.png"
    app.batMove6 = "Sprites/Bat/BatMove/BATWAF0-removebg-preview.png"

    #Bat Die
    app.batDieTimer = 0
    app.batDieIndex = 0
    app.batDie1 = "Sprites/Bat/BatDie/BATDEA0-removebg-preview.png"
    app.batDie2 = "Sprites/Bat/BatDie/BATDEB0-removebg-preview.png"
    app.batDie3 = "Sprites/Bat/BatDie/BATDEC0-removebg-preview.png"
    app.batDie4 = "Sprites/Bat/BatDie/BATDED0-removebg-preview.png"
    app.batDie5 = "Sprites/Bat/BatDie/BATDEE0-removebg-preview.png"
    app.batDie6 = "Sprites/Bat/BatDie/BATDEF0-removebg-preview.png"

    ########################################### Kos Sprite
    app.kosOnScreen = False
    app.kosMoving = False
    app.kosAttacking = False
    app.kosDying = False
    #Kos Move
    app.kosMoveTimer = 0
    app.kosMoveIndex = 0
    app.kosMove1 = "Sprites/Kos/KosWalk/Noblfia0-removebg-preview.png"
    app.kosMove2 = "Sprites/Kos/KosWalk/Noblwaa0-removebg-preview.png"
    app.kosMove3 = "Sprites/Kos/KosWalk/Noblwab0-removebg-preview.png"
    app.kosMove4 = "Sprites/Kos/KosWalk/Noblwac0-removebg-preview.png"
    app.kosMove5 = "Sprites/Kos/KosWalk/Noblwad0-removebg-preview.png"
    app.kosMove6 = "Sprites/Kos/KosWalk/Noblwae0-removebg-preview.png"
    app.kosMove7 = "Sprites/Kos/KosWalk/Noblwaf0-removebg-preview.png"

    #Kos Attack
    app.kosAttackTimer = 0
    app.kosAttackIndex = 0
    app.kosAttack1 = "Sprites/Kos/KosAttack/Noblata0-removebg-preview.png"
    app.kosAttack2 = "Sprites/Kos/KosAttack/Noblatb0-removebg-preview.png"
    app.kosAttack3 = "Sprites/Kos/KosAttack/Noblatc0-removebg-preview.png"
    app.kosAttack4 = "Sprites/Kos/KosAttack/Noblatd0-removebg-preview.png"
    app.kosAttack5 = "Sprites/Kos/KosAttack/Noblate0-removebg-preview.png"
    app.kosAttack6 = "Sprites/Kos/KosAttack/Noblatf0-removebg-preview.png"

    #Kos Die
    app.kosDieTimer = 0
    app.kosDieIndex = 0
    app.kosDie1 = "Sprites/Kos/KosDie/Nobldea0-removebg-preview.png"
    app.kosDie2 = "Sprites/Kos/KosDie/NOBLDEB0-removebg-preview.png"
    app.kosDie3 = "Sprites/Kos/KosDie/NOBLDEC0-removebg-preview.png"
    app.kosDie4 = "Sprites/Kos/KosDie/NOBLDED0-removebg-preview.png"
    app.kosDie5 = "Sprites/Kos/KosDie/NOBLDEE0-removebg-preview.png"
    app.kosDie6 = "Sprites/Kos/KosDie/NOBLDEF0-removebg-preview.png"



    setActiveScreen("playScreen")
    startNewGame(app)

def startNewGame(app):
    app.weapon = 0
    app.level = 0
    app.diffIndex = 0
    app.fov = math.pi
    app.paused = False
    app.health = 100
    app.weapon = Wrench(Weapon)
    app.victory = False
    app.defeat = False
    app.startTime = 0
    app.damaged = False
    app.hit = False
    app.inStartWidth = False
    app.logoIncreasing = True
    app.logoTimer = 0
    app.logoScale = 0.7
    app.wrenchTimer = 0
    app.wrenchIndex = 0
    app.plasmaTimer = 0
    app.plasmaIndex = 0
    app.ghostOnScreen = False
    app.ghostMoving = False
    app.ghostAttacking = False
    app.ghostDying = False
    app.ghostMoveTimer = 0
    app.ghostMoveIndex = 0
    app.ghostAttackTimer = 0
    app.ghostAttackIndex = 0
    app.ghostDieTimer = 0
    app.ghostDieIndex = 0
    app.batOnScreen = False
    app.batMoving = False
    app.batDying = False
    app.batMoveTimer = 0
    app.batMoveIndex = 0
    app.batDieTimer = 0
    app.batDieIndex = 0
    app.kosOnScreen = False
    app.kosMoving = False
    app.kosAttacking = False
    app.kosDying = False
    app.kosMoveTimer = 0
    app.kosMoveIndex = 0
    app.kosAttackTimer = 0
    app.kosAttackIndex = 0
    app.kosDieTimer = 0
    app.kosDieIndex = 0

class Weapon:
    def __init__(self, name):
        self.name = name
 
class Wrench(Weapon):
    def __init__(self, name):
        super().__init__(name)
        self.range = 20
        self.damage = 100
       
    def __repr__(self):
        return 'Wrench'

class Blaster(Weapon):
    def __init__(self, name):
        super().__init__(name)
        self.range = 100
        self.damage = 100
       
    def __repr__(self):
        return 'Blaster'

class Enemy:
    def __init__(self,row,col, sprite):
        self.row = row
        self.col = col
        self.sprite = sprite
        self.speed = 5

class Player:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.speed = 7
   
def loadSound(relativePath):
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)
   
def inBounds(leftX, topY, width, height, x, y):
    return (leftX <= x <= leftX + width) and (topY <= y <= topY + height)
   
def radiansToDegrees(n):
    return math.floor((n / math.pi) * 180)

def drawImageHelper(image, x, y, resizeFactor):
    imageWidth, imageHeight = getImageSize(image)
    drawImage(image, x, y, width = imageWidth * resizeFactor, height = imageHeight * resizeFactor, align = "center")
   

def setBoard(app):
    app.rows = len(app.matrix[app.index])
    app.cols = len(app.matrix[app.index][0])
    app.boardLeft = 50
    app.boardTop = 50
    app.boardWidth = 500
    app.boardHeight = 500
    app.height = 500
    app.width = 600
    app.gameOver = False

def setChars(app):
    if(app.index == 0):
        app.keyC = (20,10)
        app.player = Player(5,15) #sets player's starting position based on row and column
        app.enemy = Enemy(7,28,2) #same as player, but adds third
    else:
        app.keyC = (10,10)
        app.plater = Player(30,15)
        app.enemy = Enemy(20,10,2)
    width, height = getCellSize(app)
    app.player.pixelX, app.player.pixelY = getCellLeftTop(app, app.player.row, app.player.col)
    app.player.pixelX += width //2
    app.player.pixelY += height //2
    app.enemy.pixelX, app.enemy.pixelY = getCellLeftTop(app, app.enemy.row, app.enemy.col)
    app.enemy.pixelX += width //2
    app.enemy.pixelY += height //2

#from library, sets a grid with the matrix in onAppStart and then finds a path
def setEnemyPath(app,index):
    app.gameOver = False
    if(index == 0):
        app.elevatorIndex = [(1,9),(2,18)]
        grid = Grid(matrix=app.matrix[app.index])
        start = grid.node(app.enemy.col, app.enemy.row)
        end = grid.node(app.player.col, app.player.row)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        app.path = path
    if(index == 1):
        app.elevatorIndex = [(29,15),(30,20)]
        grid = Grid(matrix=app.matrix[app.index])
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
            #print(app.elevatorIndex)
            elevatorTopRow, elevatorLeftCol = app.elevatorIndex[0]
            elevatorBottomRow, elevatorRightCol = app.elevatorIndex[1]
            if (app.matrix[app.index][row][col] == 0):
                drawCell(app, row, col, None)
            elif(elevatorTopRow <= row <= elevatorBottomRow) and (elevatorLeftCol <= col <= elevatorRightCol):
                color = 'gold' if app.key else 'red'
                drawCell(app, row, col, color)

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

def drawCell(app, row, col, fill):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=fill, border='black')

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)
####################################################
# startScreen
####################################################    
def startScreen_redrawAll(app):
    drawImageHelper(app.startBackground, app.width / 2, app.height / 2, 1)
    drawImageHelper(app.logo, app.width / 2 - 4, app.height / 7.4, app.logoScale / 1.72)
    drawScotty(app)
    drawStartButton(app)
    drawLabel("By: Connor, Josh, Ricky & Ben", app.width / 2, 487, size = 17, fill = "white")

def drawScotty(app):
    scottyList = [app.scotty1,app.scotty2,app.scotty3,app.scotty4,app.scotty5,app.scotty6,app.scotty7,app.scotty8]
    drawImageHelper(scottyList[app.scottyIndex], app.scottyCx, 366, 0.7)

def drawStartButton(app):
    if app.inStartWidth:
        drawRect(app.width / 2, 435, 195, 65, fill = 'red',align = "center")
    drawRect(app.width / 2, 435, 190, 60, fill = 'black', opacity = 100, border = "red", align = "center")
    drawLabel('Start', app.width/2, 435, size = 33, fill = "red", bold = True)
   
def startScreen_onMousePress(app, mouseX, mouseY):
    
    if inBounds(205, 405, 190, 60, mouseX, mouseY):
        startNewGame(app)
        setActiveScreen('settingsScreen')

def inBounds(leftX, topY, width, height, x, y):
    return (leftX <= x <= leftX + width) and (topY <= y <= topY + height)

def startScreen_onMouseMove(app, mouseX, mouseY):
    if inBounds(205, 405, 190, 60, mouseX, mouseY):
        app.inStartWidth = True
    else:
        app.inStartWidth = False

def startScreen_onStep(app):
    app.logoTimer += 1
    if app.logoTimer % 2 == 0:
        if app.logoIncreasing:
            app.logoScale += 0.005
            if app.logoScale >= 0.7:
                app.logoIncreasing = False
        else:
            app.logoScale -= 0.005
            if app.logoScale < 0.6:
                app.logoIncreasing = True
    app.scottyTimer += 1
    app.scottyCx -= 2
    if app.scottyTimer % 3 == 0:
        if app.scottyCx < 46:
            app.scottyCx = app.width - 20
        if app.scottyIndex < 7:
            app.scottyIndex += 1
        else:
            app.scottyIndex = 0


####################################################
# settingsScreen
####################################################
def settingsScreen_redrawAll(app):
    drawImageHelper(app.weanCube, app.width / 2, app.height / 2, 1.19)
    drawImageHelper(app.settingsText, app.width / 2, 60, 0.3)
   
    drawBackButton(app)
    drawInfoButton(app)
    drawDifficultyButton(app)
    drawFovButton(app)
   

def drawDifficultyButton(app):
    drawRect(app.width/2 - app.width/10, app.height/3 - app.height/14, app.width/5, app.height/7, fill = rgb(230, 125, 117), opacity = 80)
    drawLabel(f'{app.difficulty[app.diffIndex]}', app.width/2, app.height/3, size = 20)
   
    drawRect(app.width/2 - app.width/5.5, app.height/3 - app.height/14, app.width/15, app.height/7, fill = rgb(230, 125, 117), opacity = 80)
    drawRegularPolygon(app.width/2 - app.width/5.5 + app.width/30, app.height/3, 10, 3, rotateAngle = 270)
   
    drawRect(app.width/2 + app.width/8.7, app.height/3 - app.height/14, app.width/15, app.height/7, fill = rgb(230, 125, 117), opacity = 80)
    drawRegularPolygon(app.width/2 + app.width/8.7 + app.width/30, app.height/3, 10, 3, rotateAngle = 90)

def drawFovButton(app):
    drawRect(app.width/2 - app.width/10, app.height/1.79 - app.height/14, app.width/5, app.height/7, fill = rgb(230, 125, 117), opacity = 80)
    drawLabel(f'{radiansToDegrees(app.fov)}', app.width/2, app.height/1.79, size = 20)
   
    drawRect(app.width/2 - app.width/5.5, app.height/1.79 - app.height/14, app.width/15, app.height/7, fill = rgb(230, 125, 117), opacity = 80)
    drawRegularPolygon(app.width/2 - app.width/5.5 + app.width/30, app.height/1.79, 10, 3, rotateAngle = 270)
   
    drawRect(app.width/2 + app.width/8.7, app.height/1.79 - app.height/14, app.width/15, app.height/7, fill = rgb(230, 125, 117), opacity = 80)
    drawRegularPolygon(app.width/2 + app.width/8.7 + app.width/30, app.height/1.79, 10, 3, rotateAngle = 90)
   
   
def drawBackButton(app):
    drawRect(app.width/1.1 - app.width/12, app.height/10- app.height/16, app.width/6, app.height/8, fill = rgb(230, 125, 117), opacity = 80)
    drawLabel('Back', app.width/1.1 + 20, app.height/10, size = 14)
    drawLine(app.width/1.1 - app.width/12 + 10, app.height/10, app.width/1.1, app.height/10, arrowStart = True )

   
def drawInfoButton(app):
    drawRect(app.width/2 - app.width/10, app.height/1.25 - app.height/14, app.width/5, app.height/7, fill = rgb(230, 125, 117), opacity = 80)
    drawLabel('Next', app.width/2, app.height/1.25, size = 20)
   
def settingsScreen_onMousePress(app, mouseX, mouseY):
    if inBounds(app.width/1.1 - app.width/12, app.height/10- app.height/16, app.width/6, app.height/8, mouseX, mouseY):
        setActiveScreen('startScreen')
       
    elif inBounds(app.width/2 - app.width/10, app.height/1.25 - app.height/14, app.width/5, app.height/7, mouseX, mouseY):
        setActiveScreen('helpScreen')
       
    elif inBounds(app.width/2 - app.width/5.5, app.height/3 - app.height/14, app.width/15, app.height/7,mouseX, mouseY):
        if app.diffIndex > 0:
            app.diffIndex -= 1
   
    elif inBounds(app.width/2 + app.width/8.7, app.height/3 - app.height/14, app.width/15, app.height/7,mouseX, mouseY):
        if app.diffIndex < 2:
            app.diffIndex += 1
       
    elif inBounds(app.width/2 - app.width/5.5, app.height/1.79 - app.height/14, app.width/15, app.height/7,mouseX, mouseY):
        if app.fov > math.pi / 3:
            app.fov -= math.pi / 8

    elif inBounds(app.width/2 + app.width/8.7, app.height/1.79 - app.height/14, app.width/15, app.height/7,mouseX, mouseY):
        if app.fov < 2*math.pi:
            app.fov += math.pi / 8
   
   

####################################################
# helpScreen
####################################################
def helpScreen_redrawAll(app):
    drawImageHelper(app.weanCube, app.width / 2, app.height / 2, 1.19)
    drawImageHelper(app.howToPlayText, app.width / 2, 60, 0.4)
    drawRect(app.width / 2, 192, 450, 172, align = "center", opacity = 80)
    drawLabel("Objective:", app.width / 2, 125, size = 20,fill = "white", bold = True)
    drawLabel("Your task is to escape from Wean Hall. If it", 90, 150, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("wasn't scary enough on its own, there will", 90, 175, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("also be monsters hunting you down. Make", 90, 200, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("your way through three levels and defeat the", 90, 225, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("secret boss to escape!", 90, 250, size = 20, fill = "white", bold = True, align = "left")

    drawRect(75, 395, 225, 185, align = "left", opacity = 80)
    drawLabel("Key Controls:", 180, 320, size = 20, fill = "white", bold = True)
    drawLabel("Forward: Up key", 90, 345, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("Back: Down key", 90, 370, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("Pause: P", 90, 395, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("Wrench: 1", 90, 420, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("Plasma Gun: 2", 90, 445, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("Map: M", 90, 470, size = 20, fill = "white", bold = True, align = "left")
    

    drawBackButton(app)
   
    drawPlayButton(app)

def drawPlayButton(app):
    if app.inStartWidth:
        drawRect(527.5, 380, 195, 65, fill = 'red',align = "right")
    drawRect(525, 380, 190, 60, fill = 'black', opacity = 100, border = "red", align = "right")
    drawLabel('Play', 430, 380, size = 33, fill = "red", bold = True, align = "center")

def helpScreen_onMousePress(app, mouseX, mouseY):
    if inBounds(app.width/1.1 - app.width/12, app.height/10- app.height/16, app.width/6, app.height/8, mouseX, mouseY):
        setActiveScreen('settingsScreen')
    elif inBounds(525 - 190, 380 - 30, 190, 60, mouseX, mouseY):
        setActiveScreen('help2Screen')

####################################################
# help2Screen SECOND HOW TO PLAY FOR AIMING
####################################################
def help2Screen_redrawAll(app):
    drawImageHelper(app.weanCube, app.width / 2, app.height / 2, 1.19)
    drawImageHelper(app.howToPlayText, app.width / 2, 60, 0.4)
    drawRect(app.width / 2, 192, 450, 172, align = "center", opacity = 80)
    drawLabel("Aiming:", app.width / 2, 125, size = 20,fill = "white", bold = True)
    drawLabel("The camera will pick up the laser pointer's", 90, 150, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("position and translate it into looking left,", 90, 175, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("right, or remaining stationary. Click to attack", 90, 200, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("when lined up with an enemy, Reference the", 90, 225, size = 20, fill = "white", bold = True, align = "left")
    drawLabel("diagram to see the aiming grid.", 90, 250, size = 20, fill = "white", bold = True, align = "left")

    drawRect(75, 395, 225, 185, align = "left", opacity = 80)
    drawRect(77, 304, 221, 40, fill = "red")
    drawLabel("Left", 115, 410, size = 16, fill = "white", bold = True)
    drawLabel("Stay", 190, 410, size = 16, fill = "white", bold = True)
    drawLabel("Right", 265, 410, size = 16, fill = "white", bold = True)
    drawLine(153, 344, 153, 488, fill = "white")
    drawLine(229, 344, 229, 488, fill = "white")
    drawLabel("Don't aim up here", 190, 325, size = 20, fill = "white", bold = True, align = "center")

    drawBackButton(app)
    drawPlayButton(app)

def help2Screen_onMousePress(app, mouseX, mouseY):
    if inBounds(app.width/1.1 - app.width/12, app.height/10- app.height/16, app.width/6, app.height/8, mouseX, mouseY):
        setActiveScreen('helpScreen')
    elif inBounds(525 - 190, 380 - 30, 190, 60, mouseX, mouseY):
        setActiveScreen('gridGameScreen')




################################################################## Play gridGame

def gridGameScreen_redrawAll(app):
    drawBoard(app)
    if app.gameOver:
        drawGameOver(app)
    else:
        drawPlayer(app)
        drawEnemy(app)
        drawWeapon(app)
        drawHealth(app)
        #print(app.key)
        if(not app.key):
            drawKey(app)

def drawHealth(app):
    if app.health > 75:
        color = 'lightGreen'
    elif app.health > 50:
        color = 'yellow'
    elif app.health > 25:
        color = 'orange'
    else:
        color = 'red'
       
    if app.health > 0:
        width = (app.health * app.width/5.7 / 100)
    else:
        width = 0.00000001
       
   
    drawRect(app.width/20 + 3, app.height - 20, width, app.height/25, fill = color)
    drawRect(app.width/20 + 3, app.height - 20, app.width/5.7, app.height/25, fill = None, border = 'black')
    drawLabel(f'{app.health}', app.width/20 + 10, app.height - 7, size = 12, align = 'bottom-left', bold = True)

def drawGameOver(app):
    drawLabel('TEST',app.width // 2, app.height // 2, fill = 'red', size = 16)

def drawPlayer(app):
    drawCircle(app.player.pixelX, app.player.pixelY, app.radius, fill='blue')

def drawEnemy(app):
    drawCircle(app.enemy.pixelX, app.enemy.pixelY, app.radius, fill = 'red')

def drawWeapon(app):
    if str(app.weapon) == "Wrench":
        drawLine(app.player.pixelX, app.player.pixelY, app.player.pixelX + math.cos(app.angle) * 20, app.player.pixelY + math.sin(app.angle) * 20, lineWidth = 10)
    elif str(app.weapon) == "Blaster":
        drawRect(app.player.pixelX, app.player.pixelY, 58,60, fill = "gold", opacity = 50)

def drawKey(app):
    x,y = convertToPixel(app, app.keyC)
    drawRect(x,y,5,5, fill='green')

def gridGameScreen_onKeyPress(app, key):
    if key == 'up':
        if app.health < 100:
            app.health += 5
    elif key == 'down':
        if app.health > 0:
            app.health -= 5
        if app.health <= 0:
            app.defeat = True
    elif (key == 'space'):
        app.attack = True
    if key == 'w':
        movePlayer(app,-1,0)
    elif key == 's':
        movePlayer(app,1,0)
    elif key == 'a':
        movePlayer(app,0,-1)
    elif key == 'd':
        movePlayer(app,0,1)
    
def gridGameScreen_onMousePress(app, x, y):
    app.attack = True

def gridGameScreen_onKeyHold(app, key):
    if 'w' in key:
        movePlayer(app,-1,0)
    elif 's' in key:
        movePlayer(app,1,0)
    elif 'a' in key:
        movePlayer(app,0,-1)
    elif 'd' in key:
        movePlayer(app,0,1)
    if 'left' in key:
        app.angle -= 0.2
    elif 'right' in key:
        app.angle += 0.2
    #app.soundDic['footsteps'].play()

def movePlayer(app,drow,dcol):
    #change stepsPerSecond to speed wanted
    app.player.pixelX += dcol * app.player.speed
    app.player.pixelY += drow * app.player.speed
    app.player.row, app.player.col = getCell(app, app.player.pixelX, app.player.pixelY)
    if(app.matrix[app.index][app.player.row][app.player.col] == 0):
        app.player.pixelX -= dcol * app.player.speed
        app.player.pixelY -= drow * app.player.speed
        app.player.row, app.player.col = getCell(app, app.player.pixelX, app.player.pixelY) 

def moveEnemy(app,drow,dcol):
    app.enemy.pixelX += dcol * app.enemy.speed
    app.enemy.pixelY += drow * app.enemy.speed
    

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
    if(app.path == None or len(app.path) < 1):
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

def gridGameScreen_onStep(app):
    app.steps += 1
    #checkSound(app)
    if not app.gameOver:
        setEnemyPath(app,app.index)
        enemyPlacement(app)
        if(app.attack):
            app.attackTimer += 1
            if(app.attackRange):
                killEnemy(app)
            if(app.attackTimer % 10 == 0):
                app.attack = False
                app.attackTimer = 0
        if app.hit:
            if(app.hitTimer % 20 == 0):
                app.health -= 5
            app.hitTimer += 1
        checkPlacement(app)
    else:
        setChars(app)
        setEnemyPath(app,app.index)

def killEnemy(app):
    width, height = getCellSize(app)
    app.enemy = Enemy(7,28,2) #same as player, but adds third input for type of enemy
    app.enemy.pixelX, app.enemy.pixelY = getCellLeftTop(app, app.enemy.row, app.enemy.col)
    app.enemy.pixelX += width //2
    app.enemy.pixelY += height //2
    enemyPlacement(app)

def checkPlacement(app):
    playerRow, playerCol = app.player.row, app.player.col
    keyRow, keyCol = app.keyC
    elevatorTopRow, elevatorLeftCol = app.elevatorIndex[0]
    elevatorBottRow, elevatorRightCol = app.elevatorIndex[1]
    # print(keyRow,keyCol)
    # print(playerRow,playerCol)
    if (app.enemy.col -1 <= app.player.col <= app.enemy.col + 1) and (app.enemy.row - 1 <= app.player.row <= app.player.row + 1):
        app.attackRange = True
    else:
        app.attackRange = False
    if app.enemy.col == app.player.col and app.enemy.row == app.player.row:
        app.hit = True
    else:
        app.hit = False
    if (keyCol - 1 <= playerCol <= keyCol + 1) and (keyRow - 1 <= playerRow <= keyRow + 1):
        app.key = True
    if app.key and ((elevatorTopRow <= playerRow <= elevatorBottRow) and (elevatorLeftCol <= playerCol <= elevatorRightCol)):
        app.index += 1
        if(app.index == 2):
            setActiveScreen('playScreen')
        app.gameOver = True

def enemyPlacement(app):
    targetX, targetY = convertToPixel(app,(app.enemy.row, app.enemy.col)) #target next Cell
    dx, dy = getDir(app)
    if(len(app.path) == 1):
        setEnemyPath(app,app.index)
    if ((abs(app.enemy.pixelX - targetX) < 10) and dx != 0) or (dy != 0 and (abs(app.enemy.pixelY - targetY) < 10)) or (dx == 0 and dy == 0):
        app.lastPath = app.path.pop(0)
        if(len(app.path) < 1):
            setEnemyPath(app,app.index)
        else:
            col, row = app.path[0]
            app.enemy.row = row
            app.enemy.col = col
            setEnemyPath(app,app.index)
    else:
        moveEnemy(app,dy,dx)
    if app.steps % 3 == 0:
        setEnemyPath(app,app.index)

#####################################################################




####################################################
# playScreen
####################################################
def playScreen_redrawAll(app):
    
    if app.paused:
        drawLabel('Paused', app.width/2, 50, size = 24)
        drawRect(0, 0, app.width, app.height, fill = 'white', opacity = 50)
        drawLabel('Press r to resume', app.width/2, 80, size = 24)
        return

    drawLabel('Playing', app.width/2, 50, size = 24)
    drawLabel('Press p to pause', app.width/2, 75, size = 16)
    drawLabel('Press m to see minimap', app.width/2, 100, size = 16)
    drawRect(0, 420, app.width, app.height - 420, fill = "gray")
    drawLine(175, 420, 175, app.height, fill = rgb(233,233,233), lineWidth = 4)
    drawLabel("Health", 87, 435, size = 17, fill = rgb(233,233,233), bold = True)
    drawLine(300, 420, 300, app.height, fill = rgb(233,233,233), lineWidth = 4)
    drawLabel("Weapon", 235, 440, size = 17, fill = rgb(233,233,233), bold = True)
    drawLine(445, 420, 445, app.height, fill = rgb(233,233,233), lineWidth = 4)
    if str(app.weapon) == "Wrench":
        drawRect(175, 455, 65,60, fill = "gold", opacity = 50)
    elif str(app.weapon) == "Blaster":
        drawRect(242, 455, 58,60, fill = "gold", opacity = 50)
    wrenchLogoW, wrenchLogoH = getImageSize(app.wrenchLogo)
    drawImage(app.wrenchLogo, 210, app.height, width = wrenchLogoW * 0.2, height = wrenchLogoH * 0.2, align = "bottom")
    plasmaLogoW, plasmaLogoH = getImageSize(app.plasmaLogo)
    drawImage(app.plasmaLogo, 238, app.height, width = plasmaLogoW * 0.38, height = plasmaLogoH * 0.38, align = "bottom")
    drawLine(445, 420, 445, app.height, fill = rgb(233,233,233), lineWidth = 4)
    

    #health bar    
       
    if app.health > 75:
        color = 'lightGreen'
    elif app.health > 50:
        color = 'yellow'
    elif app.health > 25:
        color = 'orange'
    else:
        color = 'red'
       
    if app.health > 0:
        width = (app.health * app.width/5.7 / 100)
    else:
        width = 0.00000001
       
   
    drawRect(app.width/20 + 3, 455, width, app.height/25, fill = color)
    drawRect(app.width/20 + 3, 455, app.width/5.7, app.height/25, fill = None, border = 'black')
    drawLabel(f'{app.health}', app.width/20 + 8, 455+app.height/50, size = 12, align = 'left', bold = True)
   
    #weapon bar
    drawLabel(f'{app.weapon}', app.width/1.25 + app.width/11.4 - 160, 440, size = 17, fill = rgb(233,233,233), bold = True)
 
    if app.weapon.damage > 75:
        dmg = 'lightGreen'
    elif app.weapon.damage > 50:
        dmg = 'yellow'
    elif app.weapon.damage > 25:
        dmg = 'orange'
    else:
        dmg = 'red'
       
    if app.weapon.range > 75:
        rng = 'lightGreen'
    elif app.weapon.range > 50:
        rng = 'yellow'
    elif app.weapon.range > 25:
        rng = 'orange'
    else:
        rng = 'red'
   
    drawRect(app.width/1.25 - 160, 452, app.weapon.damage * app.width/5.7 / 100, app.height/25, fill = dmg)
    drawRect(app.width/1.25 - 160, 452, app.width/5.7, app.height/25, fill = None, border = 'black')
    drawLabel('DMG', app.width/1.25 + 5 - 160, 452+app.height/50, size = 10, align = 'left')
   
    drawRect(app.width/1.25 - 160, 475, app.weapon.range * app.width/5.7 / 100, app.height/25, fill = rng)
    drawRect(app.width/1.25 - 160, 475, app.width/5.7, app.height/25, fill = None, border = 'black')
    drawLabel('Range', app.width/1.25 + 5 - 160, 475 + app.height/50, size = 10, align = 'left')

    ##################### Draw weapon
    if str(app.weapon) == "Wrench":
        wrenchList = [app.wrench1,app.wrench2,app.wrench3,app.wrench4,app.wrench5,app.wrench6,app.wrench7,app.wrench8,app.wrench9,app.wrench10,app.wrench11,app.wrench12,app.wrench13,app.wrench14,app.wrench15,app.wrench16,app.wrench17]
        wrenchW, wrenchH = getImageSize(wrenchList[app.wrenchIndex])
        drawImage(wrenchList[app.wrenchIndex], 360, 420, width = wrenchW * 1, height = wrenchH * 1, align = "bottom")
    elif str(app.weapon) == "Blaster":
        plasmaList = [app.plasma1,app.plasma2,app.plasma3,app.plasma4,app.plasma5,app.plasma6,app.plasma7,app.plasma8,app.plasma9,app.plasma10,app.plasma11,app.plasma12,app.plasma13,app.plasma14,app.plasma15,app.plasma16,app.plasma17,app.plasma18,app.plasma19,app.plasma20,app.plasma21,app.plasma22,app.plasma23,app.plasma24,app.plasma25,app.plasma26,app.plasma27,app.plasma28,app.plasma29]
        plasmaW, plasmaH = getImageSize(plasmaList[app.plasmaIndex])
        drawImage(plasmaList[app.plasmaIndex], 300, 420, width = plasmaW * 1.4, height = plasmaH * 1.4, align = "bottom")

    drawCrosshair(app)

    if app.damaged:
        drawRect(0,0,app.width, 420, fill = "red", opacity = 30)

def playScreen_onKeyPress(app, key):
    if key == 'p':
        app.paused = True
       
    elif key == 'r':
        app.paused = False
       
    elif key == 'm':
        setActiveScreen('miniMapScreen')
   
    elif key == 'up':
        if app.health < 100:
            app.health += 5
    elif key == 'down':
        if app.health > 0:
            app.health -= 5
        if app.health <= 0:
            app.defeat = True
    elif key == "1":
        app.weapon = Wrench(Weapon)
    elif key == "2":
        app.weapon = Blaster(Weapon)
    
def playScreen_onStep(app):
    if app.paused:
        return
    if app.hit:
        app.startTime = 0
        app.damaged = True
        app.hit = False
    if app.damaged:
        app.startTime += 1
        if app.startTime == 10:
            app.damaged = False
    if app.victory:
        setActiveScreen("victoryScreen")
    elif app.defeat:
        setActiveScreen("defeatScreen")
    ################################### Shooting
    if app.swinging:
        app.wrenchTimer += 1
        if app.wrenchTimer % 2 == 0 or app.wrenchTimer % 3 == 0:
            if app.wrenchIndex < 16:
                app.wrenchIndex += 1
            else:
                app.wrenchIndex = 0
                app.swinging = False
    ################### Plasma Blaster Animation
    elif app.shooting:
        app.plasmaTimer += 1
        if app.plasmaTimer % 3 == 0:
            if app.plasmaIndex < 28:
                app.plasmaIndex += 1
            else:
                app.plasmaIndex = 0
                app.shooting = False
    

def playScreen_onMousePress(app, mouseX, mouseY):
    if str(app.weapon) == "Wrench":
        if app.swinging == True:
            return
        elif app.swinging == False:
            app.swinging = True
    elif str(app.weapon) == "Blaster":
        if app.shooting == True:
            return
        elif app.shooting == False:
            app.shooting = True


def drawCrosshair(app):
    #Call a helper function canKill(app) that returns true if an enemy is aligned with crosshair and in range otherwise false
    if canKill(app):
        #Enemy can be damaged with click according to crosshair
        drawLine(app.width / 2, 235, app.width / 2, 245, fill = rgb(148, 31, 52), lineWidth = 3)
        drawLine(app.width / 2, 265, app.width / 2, 275, fill = rgb(148, 31, 52), lineWidth = 3)
        drawLine(app.width / 2 - 20, 255, app.width / 2 - 10, 255, fill = rgb(148, 31, 52), lineWidth = 3)
        drawLine(app.width / 2 + 10, 255, app.width / 2 + 20, 255, fill = rgb(148, 31, 52), lineWidth = 3)
    else:
        #Crosshair not on enemy in range
        drawLine(app.width / 2, 235, app.width / 2, 245, fill = "cyan", lineWidth = 3)
        drawLine(app.width / 2, 265, app.width / 2, 275, fill = "cyan", lineWidth = 3)
        drawLine(app.width / 2 - 20, 255, app.width / 2 - 10, 255, fill = "cyan", lineWidth = 3)
        drawLine(app.width / 2 + 10, 255, app.width / 2 + 20, 255, fill = "cyan", lineWidth = 3)

def canKill(app):
    return False





####################################################
# victoryScreen
####################################################
def victoryScreen_redrawAll(app):
    drawImageHelper(app.weanCube, app.width / 2, app.height / 2, 1.19)
    drawLabel('You Escaped From Wean!', app.width/2, 125, size = 45, bold = True)
    drawHomeButton(app)

def drawHomeButton(app):
    if app.inStartWidth:
        drawRect(app.width / 2, 370, 195, 65, fill = 'red',align = "center")
    drawRect(app.width / 2, 370, 190, 60, fill = 'black', opacity = 100, border = "red", align = "center")
    drawLabel('Home', app.width/2, 370, size = 33, fill = "red", bold = True)

def victoryScreen_onMousePress(app, mouseX, mouseY):
    if inBounds(205, 340, 190, 60, mouseX, mouseY):
        setActiveScreen('startScreen')


####################################################
# lossScreen
####################################################
def defeatScreen_redrawAll(app):
    drawImageHelper(app.weanCube, app.width / 2, app.height / 2, 1.19)
    drawLabel("You Couldn't Escape!", app.width/2, 125, size = 45, bold = True)
    drawHomeButton(app)

def drawHomeButton(app):
    if app.inStartWidth:
        drawRect(app.width / 2, 370, 195, 65, fill = 'red',align = "center")
    drawRect(app.width / 2, 370, 190, 60, fill = 'black', opacity = 100, border = "red", align = "center")
    drawLabel('Home', app.width/2, 370, size = 33, fill = "red", bold = True)

def defeatScreen_onMousePress(app, mouseX, mouseY):
    if inBounds(205, 340, 190, 60, mouseX, mouseY):
        setActiveScreen('startScreen')



####################################################
# miniMapScreen
####################################################
def miniMapScreen_redrawAll(app):
    drawMiniMap(app)
   
def drawMiniMap(app):
    drawLabel('Minimap', app.width/2, 50, size = 24)
    drawLabel('Press r to resume', app.width/2, 80, size = 24)
   
   
def miniMapScreen_onKeyPress(app, key):
    if key == 'r':
        setActiveScreen('playScreen')


   
def distance(x0, x1, y0, y1):
    return ((x0-x1)**2+(y0-y1)**2)**.5


def main():
    runAppWithScreens(initialScreen='startScreen')
   
main()