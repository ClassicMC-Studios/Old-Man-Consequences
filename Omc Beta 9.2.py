import pygame
import time
import random
import string
#---- /\  /\ ----
#|  | | \/ | |
#---- |    | ____  
pygame.init()
pygame.font.init()
#Variables 
colorGray = (184,184,184)
colorBlack = (0,0,0)
colorRed = (255,0,0)
colorDR =(128,0,0)
colorMR = (153, 51, 51)
tX = 190
tY =100
tYP = 0.05
playerX = 370
playerY = 100
scene = 0
triggerBox = 0
triggerChest = 0
triggerEnd = 0
triggerFall = 0
triggerLol = False
treeRand = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,180,200,230,270,300,350]
tom = 'Stay for a while...'
display = pygame.display.set_mode((480,360))
pygame.display.set_caption('OldManConsequences')
display.fill(colorBlack)
pygame.display.flip()
gameLoop = False  
running = True
#Redraw screen
def redraw():
  #The first redraw scene
  if scene == 1:
    omc_init()
    player_init()
    tree_init()
    if triggerBox == 1:
      pygame.draw.rect(display,colorBlack,pygame.Rect(410,140,70,70))
    lake_init()
    oldDisplay()
    
  #If the scene is 2  
  if scene == 2:
    tree_init()
    if triggerChest == 1:
      pygame.draw.rect(display,colorBlack,pygame.Rect(410,140,70,70))
    chest_init()
    player_init()
    oldDisplay()
  if scene == 3:
    pygame.draw.rect(display,colorBlack,pygame.Rect(410,140,70,70))
    omc_init()
    player_init()
    if triggerEnd == 0:
      tree_init()
    oldDisplay()
  if scene ==4:
    player_init()
    treeS4_init()
    oldDisplay()
#Clean the screen
def dFill():
  display.fill(colorBlack)
#Blit text items
def blitText(text,x,y):
  display.blit(text,(x,y))
#Draw the lines on the screen  
def oldDisplay():
  titleY = 0
  for i in range(1,37):
    pygame.draw.rect(display,colorBlack,pygame.Rect(0,titleY,500,5))
    titleY +=10
#Draw the chest to the screen    
def chest_init():
  pygame.draw.rect(display,colorMR,pygame.Rect(100,100,60,30))
  pygame.draw.rect(display,colorMR,pygame.Rect(110,90,40,30))
def player_init():
  #playerHead
  pygame.draw.rect(display,colorRed,pygame.Rect(playerX+5,playerY-10,10,15))
  #playerBody
  pygame.draw.rect(display,colorRed,pygame.Rect(playerX,playerY,20,30))
  #playerArms
  pygame.draw.rect(display,colorRed,pygame.Rect(playerX-10,playerY+5,10,10))
  pygame.draw.rect(display,colorRed,pygame.Rect(playerX+20,playerY+5,10,10))
def tree_init():
  treeY = 10
  treeX = 15
  #loop to create the trees
  for i in range(1,6):
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX,treeY,20,60))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-20,treeY+30,60,20))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-10,treeY+10,40,20))
    treeY +=70
  treeY = 10  
  for i in range(1,7):
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX,treeY,20,60))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-20,treeY+30,60,20))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-10,treeY+10,40,20))
    treeX +=70
  for i in range(1,6):
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX,treeY,20,60))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-20,treeY+30,60,20))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-10,treeY+10,40,20))
    treeY+=70
  treeY -=70  
  for i in range(1,7):
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX,treeY,20,60))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-20,treeY+30,60,20))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-10,treeY+10,40,20))
    treeX -=70
  treeX = 295
  treeY = 80
  if scene == 1:
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX,treeY,20,60))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-20,treeY+30,60,20))
    pygame.draw.rect(display,colorDR,pygame.Rect(treeX-10,treeY+10,40,20)) 
def lake_init():
  pygame.draw.rect(display, colorDR,pygame.Rect(120,150,120,60))
  pygame.draw.rect(display, colorDR,pygame.Rect(120+10,150-10,100,80))
 
def omc_init():
  if scene ==1:
    pygame.draw.rect(display,colorMR,pygame.Rect(75,140,15,60))
    pygame.draw.rect(display,colorMR,pygame.Rect(65,160,15,30))
    pygame.draw.rect(display,colorMR,pygame.Rect(55,180,30,20))
    pygame.draw.rect(display,colorBlack,pygame.Rect(80,185,15,15))
    pygame.draw.rect(display,colorMR,pygame.Rect(90,150,25,10))
    pygame.draw.rect(display,colorMR,pygame.Rect(85,180,10,20))
    pygame.draw.rect(display,colorMR,pygame.Rect(85,190,20,10))
    pygame.draw.rect(display,colorMR,pygame.Rect(90,170,15,10))
  if scene ==3:
    pygame.draw.rect(display,colorMR,pygame.Rect(75+200,140,15,60))
    pygame.draw.rect(display,colorMR,pygame.Rect(65+200,160,15,30))
    pygame.draw.rect(display,colorMR,pygame.Rect(55+200,180,30,20))
    pygame.draw.rect(display,colorBlack,pygame.Rect(80+200,185,15,15))
    pygame.draw.rect(display,colorMR,pygame.Rect(90+200,150,25,10))
    pygame.draw.rect(display,colorMR,pygame.Rect(85+200,180,10,20))
    pygame.draw.rect(display,colorMR,pygame.Rect(85+200,190,20,10))
    pygame.draw.rect(display,colorMR,pygame.Rect(90+200,170,15,10))
#Random trees
def treeS4_init():
  pygame.draw.rect(display,colorDR,pygame.Rect(treeX,treeY,20,60))
  pygame.draw.rect(display,colorDR,pygame.Rect(treeX-20,treeY+30,60,20))
  pygame.draw.rect(display,colorDR,pygame.Rect(treeX-10,treeY+10,40,20))
#Runs while the project is active    
while running:
  while not gameLoop:
    #Initilize text
    myfont = pygame.font.SysFont('cmr10', 100)
    omcTitle = myfont.render('Omc', False, (255,0,0))
    myfont = pygame.font.SysFont('cmr10',20)
    textcredits = myfont.render('A remake of a minigame by, Scott Cawthon',False,(255,0,0))
    textInfo = myfont.render('Press space to begin',False,(255,0,0))
    myfont = pygame.font.SysFont('cmr10',30)
    textoldman = myfont.render(tom,False,(255,0,0))
    sadOmc = myfont.render('Leave the demon',False,(255,0,0))
    sadOmc2 = myfont.render('to his demons,',False,(255,0,0))
    sadOmc3 = myfont.render('there is nothing else',False,(255,0,0))
    endCredits = myfont.render('Made by, ClassicMC',False,(255,0,0))
    endCredits2 = myfont.render('Credit to Scott Cawthon',False,(255,0,0))
    #Draw texts
    blitText(omcTitle,tX-60,tY)
    oldDisplay()
    blitText(textcredits,5,310)
    blitText(textInfo,6,330)
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
          print(pygame.font.get_fonts())
        if event.key == pygame.K_SPACE:
          scene = 1
          gameLoop = True
      if event.type == pygame.QUIT:
        running = False
    if tY <= 100:      
      tY+=tYP
      dFill()
    else:
      tYP = -tYP
      tY -=2
    if tY <= 50:
      tYP = 0.05
  #Main game loop    
  while gameLoop:
    #Keys pressed
    keys = pygame.key.get_pressed()
    if triggerEnd ==0:
      if keys[pygame.K_LEFT]:
        playerX -= 10
        dFill()
        redraw()
        time.sleep(0.05)
      if keys[pygame.K_RIGHT]:
        playerX += 10
        dFill()
        redraw()
        time.sleep(0.05)
      if keys[pygame.K_UP]:
        playerY -=10
        dFill()
        redraw()
        time.sleep(0.05)
      if keys[pygame.K_DOWN]:
        playerY +=10
        dFill()
        redraw()
        time.sleep(0.05)
    #Main game functions
    pygame.display.flip()
    redraw()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
          print(playerX,playerY)
        #Current vanilla collision system  
        if event.key == pygame.K_SPACE:
          if scene ==1:
            if playerY >= 120:
              if playerY <= 200:
                if playerX >= 40:
                  if playerX <= 100:
                    #Talking to old man consequences
                    pygame.draw.rect(display,colorBlack,pygame.Rect(100,90,300,100))
                    blitText(textoldman,150,100)
                    pygame.display.flip()
                    time.sleep(1)
                    dFill()
                    triggerBox = 1
                    pygame.display.flip()
            if triggerBox == 1:        
              if playerY >=120:
                if playerY <=210:
                  if playerX >= 390:
                    #Changing the scene to (2)
                    scene = 2
                    dFill()
                    playerX = 60
                    playerY = 170
          if scene ==2:
            if playerY >=70:
              if playerY <= 130:
                if playerX >= 80:
                  if playerX <= 160:
                    triggerChest =1
            if triggerChest ==1:
              if playerY >=120:
                if playerY <=210:
                  if playerX >= 390:
                    scene = 3
                    dFill()
                    playerX = 60
                    playerY = 170
          if scene == 3:
            if playerY >= 120:
              if playerY <= 200:
                if playerX >= 240:
                  if playerX <= 310:
                    pygame.draw.rect(display,colorBlack,pygame.Rect(100,90,300,100))
                    blitText(sadOmc,150,100)
                    blitText(sadOmc2,150,125)
                    blitText(sadOmc3,145,150)
                    triggerEnd = 1
                    triggerLol = True
                    playerX = 160
                    playerY = 170
                    pygame.display.flip()
                    time.sleep(2)
                    dFill()
                    redraw()
                    triggerFall =1
                    while triggerLol:
                      pygame.display.flip()
                      time.sleep(5)
                      dFill()
                      time.sleep(1)
                      blitText(endCredits,100,150)
                      blitText(endCredits2,90,180)
                      pygame.display.flip()
                      time.sleep(3)
                      dFill()
                      time.sleep(1)
                      running = False
                      pygame.quit()
            if playerY >=120:
              if playerY <=210:
                if playerX >= 390:
                  treeY = random.choice(treeRand)
                  treeX = random.randrange(5, 300)
                  scene = 4
                  dFill()