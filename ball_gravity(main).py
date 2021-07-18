import random, pygame,sys,math
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1500,900))

GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)

timer=pygame.time.Clock()

ball=pygame.image.load('ball.png')
ball=pygame.transform.scale(ball,(50,50))
X0,Y0=100,600
delta=0.1
dx,dy=1,-3
g=10
i=-1
q=0.8
Vo=100
pi=math.pi
teta=80
m,m1=0,0
Vox,Voy=Vo*math.cos(pi*teta/180), Vo*math.sin(pi*teta/180)
Level=700
plotPoints=[(100,100)]

font = pygame.font.SysFont('Corbel',35)
font1 = pygame.font.SysFont('Corbel',70)

text1 = font.render('Скорость мяча до удара об пол' , True , BLUE)
text2 = font.render('Скорость мяча после отражения от пола' , True , BLUE)
text3 = font1.render('0.8' , True , BLUE)
text4 = font1.render('0.7' , True , BLUE)
text5 = font1.render('0.6' , True , BLUE)
n=0
while True:
    
    screen.fill(GREEN)
    screen.blit(text2,(400,50))
    pygame.draw.line(screen,BLUE,(400,90),(1000,90),5)
    
    pygame.draw.line(screen,BLUE,(1050,86),(1075,86),5)
    pygame.draw.line(screen,BLUE,(1050,94),(1075,94),5)
    
    screen.blit(text1,(500,100))
    i=i+1
    n=n+1
    print('n=',n)
    t=i*delta
    X=X0+Vox*t
    print('X=',X)
    X2=X
    Y=(Level-(Voy*t-g*t*t/2))
    plotPoints.append([X,Y])
    #pygame.draw.lines(screen,('red'),False,plotPoints,7)
            
    if Y>Level:
        Vo=Vo*q
        Vox,Voy=Vo*math.cos(pi*teta/180), Vo*math.sin(pi*teta/180)
        i=0
        X0=X2
        
    if X<1001:
        if m1==0:
            q=0.8
            pygame.draw.lines(screen,('red'),False,plotPoints,7)
            screen.blit(text3,(1100,55))
        if m1==1:
            q=0.7
            pygame.draw.lines(screen,('violet'),False,plotPoints,7)
            screen.blit(text4,(1100,55))
        if m1==2:
            q=0.6
            pygame.draw.lines(screen,('navy'),False,plotPoints,7)
            screen.blit(text5,(1100,55))
    
    if n==700:
        Vo=100
        Vox,Voy=Vo*math.cos(pi*teta/180), Vo*math.sin(pi*teta/180)
        m=m+1
        m1=m%3
        print('m=',m,'m1=',m1)
        n=0
        i=-1
        plotPoints.clear()
        plotPoints=[(100,100)]
        X0,Y0=100,600
        #screen.fill(GREEN)
        
    rect_ball=ball.get_rect(center=(X,Y))
    
    screen.blit(ball,rect_ball)
    pygame.draw.line(screen,BLUE,(100,Level+25),(1300,Level+25),10)
    pygame.draw.line(screen,BLUE,(102,100),(102,Level+25),10)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    timer.tick(45)
    pygame.display.update()
    
    

