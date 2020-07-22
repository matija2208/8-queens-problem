import pygame as pg
import pygamebg

n=int(input("Unesite broj n : "))
Qx=[0]*(n)
Qy=[0]*(n)
c=1
i=0
j=0
t=True

window=pygamebg.open_window(n*50,n*50,"Tabla")
def popunjavanje():
    for i in range (0,n):
        for j in range (0,n):
            if (i+j)%2==0:
                pg.draw.rect(window,(255,255,255),(j*50,i*50,50,50))
            else:
                pg.draw.rect(window,(0,0,0),(j*50,i*50,50,50))

def tekst (x,y,colour):
    pg.draw.rect(window,colour,(x*50,y*50,50,50))

def mesto():
    global i
    global j
    global c
    global Qx
    global Qy
    global n
    global t
    b=True

    if t==False:
        t=True
        popunjavanje()
        if Qx[0]==n-1:
            Qx[0]=0
            if Qy[0]==n-1:
                print("Nema resenja!!!")
                quit()
            else:
                Qy[0]+=1
        else:
            Qx[0]+=1
        tekst(Qx[0],Qy[0],(0,255,0))

    for z in range (0,c):
            if j == Qx[z] or i == Qy[z] or abs(i - Qy[z]) == abs(j - Qx[z]):
                b = False
                break
    
    if b == True:
            c+=1
            tekst(j,i,(255,0,0))
            Qx[c-1] = j
            Qy[c-1] = i 
    

    if j>=n-1:
        j=0
        if i>=n-1:
            i=0
            if c==n:
                
                e=True
                
            else:
                c=1
                t=False
        else:
            i+=1
    else:
        j+=1
    

        

popunjavanje()
Qx[0]=0
Qy[0]=0
tekst(Qx[0],Qy[0],(0,255,0))

pygamebg.frame_loop(n*n,mesto)