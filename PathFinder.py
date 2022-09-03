from typing import final
import pygame,sys,math
import numpy as np

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


board=np.ones((8,8),dtype=int)
start_y,start_x=1,6
end_y,end_x=7,0
board[start_x][start_y]=2
board[end_x][end_y]=3
logic=board
found=False
solving=True
lowestTrade=None
finalTraced=[[start_x,start_y]]
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

    
drawBoxes(board)
drawButton()

def get_adjacent_points(y,x):
    arr=[]
    
    a1,b1=x+1,y
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    a1,b1=x-1,y
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    a1,b1=x,y+1
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    a1,b1=x,y-1
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    a1,b1=x+1,y-1
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    a1,b1=x+1,y+1
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    a1,b1=x-1,y+1
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    a1,b1=x-1,y-1
    if(a1<8 and a1>=0 and b1<8 and b1>=0):
        if(board[b1][a1]!=0):
            arr.append([a1,b1])
    return arr

def getScore(points):
    length=len(points)
    arr=[]
    for i in range(length):
        point=points[i]
        x_cord=point[0]
        y_cord=point[1]
        x_end=end_y
        y_end=end_x
        x_start=start_y
        y_start=start_x
        distWithEnd=(math.dist([x_end,y_end],[x_cord,y_cord]))
        distWithFirst=(math.dist([x_start,y_start],[x_cord,y_cord]))
        ans=distWithEnd+distWithFirst
        finalArr=[x_cord,y_cord,ans]
        arr.append(finalArr)
    
    return(arr)
       
def findSmallest(score):
    lowest=[]
    lowestValue=9999999999999999999999999999999999999
    for i in range(len(score)):
        if(score[i][2]<lowestValue):
            lowest=[]
            lowest.append([score[i][0],score[i][1]])
            lowestValue=score[i][2]
        elif(score[i][2]==lowestValue):
            lowest.append([score[i][0],score[i][1]])
    return lowest


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
    
            if ans[0]>100 and ans[0]<200 and ans[1]>300 and ans[1]<350:
                while solving:
                    attached=get_adjacent_points(start_x,start_y)
                    score=getScore(attached)
                    smallest=findSmallest(score)
                    print(len(smallest))
                    start_x,start_y=smallest[0][1],smallest[0][0]
                    finalTraced.append([start_x,start_y])
                    if([end_y,end_x] in smallest):
                        print("Path Found")
                        for i in range(len(finalTraced)):
                            table=finalTraced[i]
                            board[table[0]][table[1]]=4
                            drawBoxes(board)
                            solving=False
                        break