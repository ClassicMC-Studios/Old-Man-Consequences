import pygame, time
pygame.init()
pygame.font.init()
#Variables 
colorGray = (184,184,184)
colorBlack = (0,0,0)
colorRed = (255,0,0)
colorDR =(128,0,0)
tX = 190
tY =100
tYP = 0.05
playerX = 370
playerY = 100
colorMR = (153, 51, 51)
display = pygame.display.set_mode((480,360))
pygame.display.set_caption('OldManConcequences')
display.fill(colorBlack)
pygame.display.flip()
gameLoop = False
running = True
#Clean the screen
def dFill():
  display.fill(colorBlack)
#Draw the lines on the screen  
def oldDisplay():
  titleY = 0
  for i in range(1,37):
    pygame.draw.rect(display,colorBlack,pygame.Rect(0,titleY,500,5))
    titleY +=10
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
  pygame.draw.rect(display,colorDR,pygame.Rect(treeX,treeY,20,60))
  pygame.draw.rect(display,colorDR,pygame.Rect(treeX-20,treeY+30,60,20))
  pygame.draw.rect(display,colorDR,pygame.Rect(treeX-10,treeY+10,40,20)) 
def lake_init():
  pygame.draw.rect(display, colorDR,pygame.Rect(120,150,120,60))
  pygame.draw.rect(display, colorDR,pygame.Rect(120+10,150-10,100,80))
def omc_init():
  pygame.draw.rect(display,colorMR,pygame.Rect(75,140,15,60))
  pygame.draw.rect(display,colorMR,pygame.Rect(65,160,15,30))
  pygame.draw.rect(display,colorMR,pygame.Rect(55,180,30,20))
  pygame.draw.rect(display,colorBlack,pygame.Rect(80,185,15,15))
  pygame.draw.rect(display,colorMR,pygame.Rect(90,150,25,10))
  pygame.draw.rect(display,colorMR,pygame.Rect(85,180,10,20))
  pygame.draw.rect(display,colorMR,pygame.Rect(85,190,20,10))
  pygame.draw.rect(display,colorMR,pygame.Rect(90,170,15,10))  
#Runs while the project is active    
while running:
  while not gameLoop:
    myfont = pygame.font.SysFont('cmr10', 100)
    textsurface = myfont.render('Omc', False, (255,0,0))
    myfont = pygame.font.SysFont('cmr10',20)
    textcredits = myfont.render('A remake of a minigame by, Scott Cawthon',False,(255,0,0))
    display.blit(textsurface,(tX-60,tY)) 
    oldDisplay()
    display.blit(textcredits,(5,330))
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          gameLoop = True
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
    pygame.display.flip()
    dFill()
    omc_init()
    player_init()
    tree_init()
    lake_init()
    oldDisplay()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
        gameLoop = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
      playerY +=10
      time.sleep(0.05)
    if keys[pygame.K_UP]:
      playerY -=10
      time.sleep(0.05)
    if keys[pygame.K_LEFT]:
      playerX -=10
      time.sleep(0.05)
    if keys[pygame.K_RIGHT]:
      playerX +=10
      time.sleep(0.05)  