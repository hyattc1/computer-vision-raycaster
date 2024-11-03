from cmu_graphics import *

def onAppStart(app):
    app.stepsPerSecond = 30
    app.width = 600
    app.height = 500
    app.weapon = 1

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
    app.ghostOnScreen = True
    app.ghostMoving = False
    app.ghostAttacking = False
    app.ghostDying = True
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
    app.batOnScreen = True
    app.batMoving = True
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
    app.kosOnScreen = True
    app.kosMoving = True
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

############### Helper Functions
def drawImageHelper(image, x, y, resizeFactor):
    imageWidth, imageHeight = getImageSize(image)
    drawImage(image, x, y, width = imageWidth * resizeFactor, height = imageHeight * resizeFactor, align = "center")

###############

def redrawAll(app):
    drawRect(0,0,app.width, app.height)
    if app.weapon == 0:
        wrenchList = [app.wrench1,app.wrench2,app.wrench3,app.wrench4,app.wrench5,app.wrench6,app.wrench7,app.wrench8,app.wrench9,app.wrench10,app.wrench11,app.wrench12,app.wrench13,app.wrench14,app.wrench15,app.wrench16,app.wrench17]
        wrenchW, wrenchH = getImageSize(wrenchList[app.wrenchIndex])
        drawImage(wrenchList[app.wrenchIndex], 350, 500, width = wrenchW * 1.4, height = wrenchH * 1.4, align = "bottom")
    elif app.weapon == 1:
        plasmaList = [app.plasma1,app.plasma2,app.plasma3,app.plasma4,app.plasma5,app.plasma6,app.plasma7,app.plasma8,app.plasma9,app.plasma10,app.plasma11,app.plasma12,app.plasma13,app.plasma14,app.plasma15,app.plasma16,app.plasma17,app.plasma18,app.plasma19,app.plasma20,app.plasma21,app.plasma22,app.plasma23,app.plasma24,app.plasma25,app.plasma26,app.plasma27,app.plasma28,app.plasma29]
        plasmaW, plasmaH = getImageSize(plasmaList[app.plasmaIndex])
        drawImage(plasmaList[app.plasmaIndex], 300, 500, width = plasmaW * 1.8, height = plasmaH * 1.8, align = "bottom")

    #draw Ghost
    if app.ghostOnScreen:
        if app.ghostMoving:
            ghostMoveList = [app.ghostMove1,app.ghostMove2,app.ghostMove3,app.ghostMove4,app.ghostMove5,app.ghostMove6]
            drawImageHelper(ghostMoveList[app.ghostMoveIndex], 300, 150, 0.8)
        elif app.ghostAttacking:
            ghostAttackList = [app.ghostAttack1,app.ghostAttack2,app.ghostAttack3,app.ghostAttack4,app.ghostAttack5,app.ghostAttack6]
            drawImageHelper(ghostAttackList[app.ghostAttackIndex], 150, 150, 0.8)
        elif app.ghostDying:
            ghostDieList = [app.ghostDie1,app.ghostDie2,app.ghostDie3,app.ghostDie4,app.ghostDie5,app.ghostDie6,app.ghostDie6,app.ghostDie6]
            drawImageHelper(ghostDieList[app.ghostDieIndex], 450,150,0.8)
    
    #draw Bat... do not use elif because there could be multiple types of enemies on the screen
    if app.batOnScreen:
        if app.batMoving:
            batMoveList = [app.batMove1,app.batMove2,app.batMove3,app.batMove4,app.batMove5,app.batMove6]
            drawImageHelper(batMoveList[app.batMoveIndex], 150, 400, 1)
        elif app.batDying:
            batDieList = [app.batDie1,app.batDie2,app.batDie3,app.batDie4,app.batDie5,app.batDie6,app.batDie6,app.batDie6,app.batDie6]
            drawImageHelper(batDieList[app.batDieIndex], 450, 150, 1)
    
    #draw Kos
    if app.kosOnScreen:
        if app.kosMoving:
            kosMoveList = [app.kosMove1,app.kosMove2,app.kosMove3,app.kosMove4,app.kosMove5,app.kosMove6,app.kosMove7]
            drawImageHelper(kosMoveList[app.kosMoveIndex], 300, 150, 0.8)
        elif app.kosAttacking:
            kosAttackList = [app.kosAttack1,app.kosAttack2,app.kosAttack3,app.kosAttack4,app.kosAttack5,app.kosAttack6]
            drawImageHelper(kosAttackList[app.kosAttackIndex], 150, 350, 0.8)
        elif app.kosDying:
            kosDieList = [app.kosDie1,app.kosDie2,app.kosDie3,app.kosDie4,app.kosDie5,app.kosDie6,app.kosDie6,app.kosDie6]
            drawImageHelper(kosDieList[app.kosDieIndex], 450,150,0.8)

def onStep(app):
    #################### Wrench Swing
    if app.weapon == 0:
        app.wrenchTimer += 1
        if app.wrenchTimer % 2 == 0:
            if app.wrenchIndex < 16:
                app.wrenchIndex += 1
            else:
                app.wrenchIndex = 0
    ################### Plasma Blaster Animation
    elif app.weapon == 1:
        app.plasmaTimer += 1
        if app.plasmaTimer % 3 == 0:
            if app.plasmaIndex < 28:
                app.plasmaIndex += 1
            else:
                app.plasmaIndex = 0
    
    #ghost sprite
    if app.ghostOnScreen:
        if app.ghostMoving:
            app.ghostMoveTimer += 1
            if app.ghostMoveTimer % 5 == 0:
                if app.ghostMoveIndex < 5:
                    app.ghostMoveIndex += 1
                else:
                    app.ghostMoveIndex = 0
        elif app.ghostAttacking:
            app.ghostAttackTimer += 1
            if app.ghostAttackTimer % 5 == 0:
                if app.ghostAttackIndex < 5:
                    app.ghostAttackIndex += 1
                else:
                    app.ghostAttackIndex = 0
        elif app.ghostDying:
            app.ghostDieTimer += 1
            if app.ghostDieTimer % 4 == 0:
                if app.ghostDieIndex < 7:
                    app.ghostDieIndex += 1
                else:
                    app.ghostDieIndex = 0
    #bat sprite
    if app.batOnScreen:
        if app.batMoving:
            app.batMoveTimer += 1
            if app.batMoveTimer % 5 == 0:
                if app.batMoveIndex < 5:
                    app.batMoveIndex += 1
                else:
                    app.batMoveIndex = 0
        elif app.batDying:
            app.batDieTimer += 1
            if app.batDieTimer % 4 == 0:
                if app.batDieIndex < 8:
                    app.batDieIndex += 1
                else:
                    app.batDieIndex = 0
    #kos sprite
    if app.kosOnScreen:
        if app.kosMoving:
            app.kosMoveTimer += 1
            if app.kosMoveTimer % 5 == 0:
                if app.kosMoveIndex < 6:
                    app.kosMoveIndex += 1
                else:
                    app.kosMoveIndex = 0
        elif app.kosAttacking:
            app.kosAttackTimer += 1
            if app.kosAttackTimer % 5 == 0:
                if app.kosAttackIndex < 5:
                    app.kosAttackIndex += 1
                else:
                    app.kosAttackIndex = 0
        elif app.kosDying:
            app.kosDieTimer += 1
            if app.kosDieTimer % 4 == 0:
                if app.kosDieIndex < 7:
                    app.kosDieIndex += 1
                else:
                    app.kosDieIndex = 0

def main():
    runApp()
main()