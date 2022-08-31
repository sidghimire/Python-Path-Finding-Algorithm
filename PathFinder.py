import pygame,sys,math

# Initializing Pygame
pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((300,400))
  
# Initialing Color
green = (0,150,0)
grey = (180,180,180)
black = (0,0,0)
white = (255,255,255)
red=(255,0,0)
blue=(0,0,255)
surface.fill(white)


board=[[1 for col in range(8)] for row in range(8)]
a,b=6,2
p,q=1,6
board[a][b]=2
board[p][q]=3
logic=board
found=False

def drawBoxes(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            sign=board[i][j]
            if sign==1:
                pygame.draw.rect(surface, grey, pygame.Rect(j*35+10, i*35+10, 35, 35), 1)
            if sign==0:
                pygame.draw.rect(surface, black, pygame.Rect(j*35+10, i*35+10, 35, 35))
            if sign==2:
                pygame.draw.rect(surface, green, pygame.Rect(j*35+10, i*35+10, 35, 35))
            if sign==3:
                pygame.draw.rect(surface, blue, pygame.Rect(j*35+10, i*35+10, 35, 35))
            if(sign>3):
                pygame.draw.rect(surface, grey, pygame.Rect(j*35+10, i*35+10, 35, 35))

    pygame.display.flip()
def drawButton():
    pygame.draw.rect(surface,red,pygame.Rect(100,300,100,50))
    pygame.display.flip()

def getPoint(a,b,a1,a2):
    ans=math.pow(a-a1,2)+math.pow(b-a2,2)
    ans=round(math.pow(ans,0.5),1)
    ans2=math.pow(p-a1,2)+math.pow(q-a2,2)
    ans2=round(math.pow(ans,0.5),1)
    sum=ans*10+ans2*10
    logic[a1][a2]=sum
    return sum
def calculateScore(a,b):
    val=[0]
    
    a1=a+1
    a2=b
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])
    a1=a-1
    a2=b
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])
    a1=a
    a2=b+1
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])
    a1=a
    a2=b-1
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])
    a1=a+1
    a2=b+1
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])
    a1=a+1
    a2=b-1
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])
    a1=a-1
    a2=b-1
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])
    a1=a-1
    a2=b+1
    sum=getPoint(a,b,a1,a2)
    val.append([a1,a2,sum])

    for k in range(6):
        low=()
        score=0
        
        print(low)
    
drawBoxes(board)
drawButton()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if(event.type)==pygame.MOUSEBUTTONDOWN:
            ans=pygame.mouse.get_pos()
            if ans[0]<300 and ans[1]<300:
                x=int((ans[0]-10)/35)
                y=int((ans[1]-10)/35)
                board[y][x]=0
                drawBoxes(board)
    if found==False:
        test_a,test_b=a,b
        lowest=calculateScore(test_a,test_b)
        

    if found==True:
        print("Found")