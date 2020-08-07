import pygame as pe
import pygamebg as pg
import os

n=0
window=0
k=1
colour=[]
N=[]

class gui(object):

    def crtaj():
        global N
        font = pe.font.SysFont("couriernew", 50) 
        tekst1 = font.render("Problem N kraljica", True, (0,0,170))
        tekst2 = font.render("Unesite broj n :", False, (0,204,85))
        window.blit(tekst1,(120,50))
        window.blit(tekst2, (150, 180))

        pe.draw.rect(window,(136,0,0),(125,300,550,60))

        pe.draw.polygon(window,(221,136,85),[(0,550),(0,800),(250,800)])
        pe.draw.polygon(window,(221,136,85),[(800,550),(800,800),(550,800)])

        pe.draw.rect(window,(0,136,255),(300,500,200,100))
        dugme = font.render("UNESI", True, (170, 255, 102))
        window.blit(dugme,(325,525))
       
    def dodatak():
        global N
        global window
        n=0
        m=10
        for i in range(0,len(N)):
            n*=m
            n+=N[i]
            
        pe.draw.rect(window,(136,0,0),(125,300,550,60))
        font = pe.font.SysFont("couriernew", 50)
        tekst3 = font.render(str(n),True,(0,255,131))
        window.blit(tekst3,(150,300))
    
    def brisanje():
        global N
        global window

        N.pop()
        gui.dodatak()

    def obrada():
        global N
        x=True
        while x:
            for dog in pe.event.get():
                if dog.type == pe.KEYDOWN:
                    d=dog.key
                    if dog.key != pe.K_RETURN:
                        if dog.key != pe.K_BACKSPACE and dog.key != pe.K_DELETE:
                            if int(d) >= 48 and int(d) <= 57:
                                N.append(int(d-48))
                                gui.dodatak()
                            elif int(d) >= 256 and int(d) <= 265:
                                N.append(int(d-256))
                                gui.dodatak()
                        elif len(N) > 0:
                            gui.brisanje()
                        pe.display.update()
                    else:
                        x=False
                        break
                elif dog.type == pe.MOUSEBUTTONUP:
                    kordinate=dog.pos
                    if (kordinate[0] >= 300 and kordinate[0] <= 500) and (kordinate[1] >= 500 and kordinate[1] <= 600):
                        x=False
                        break

                elif dog.type == pe.QUIT:
                    pe.quit()
                    return 0

    def inicijalizacija():
        global window
        global N
        global n
        global k

        window=pg.open_window(800,800,"N queens problem")
        
        while n<4:
            N=[]
            n=0
            window.fill((0,0,0))

            gui.crtaj()
            pe.display.update()
            gui.obrada()

            for i in range(0,len(N)):
                n*=10
                n+=N[i]
        
        
        k=800//n

        window.fill((0,0,0))
        ispis.popunjavanje()
        pe.display.update()

        return int(n)
            

def inicijalizacija_boja():
    global n
    global colour
    red=255
    green=0
    blue=0
    
    if n>=6:
        g1=True
        r2=False
        b1=False
        g2=False
        r1=False
        b2=False
        
        for i in range(0,n):
            step=1530//n

            if g1==True:
                if green+step<=255:
                    green+=step
                else:
                    g1=False
                    r2=True
                    red-=step
            elif r2==True:
                if red-step>=0:
                    red-=step
                else:
                    r2=False
                    b1=True
                    blue+=step
            elif b1==True:
                if blue+step<=255:
                    blue+=step
                else:
                    b1=False
                    g2=True
                    green-=step
            elif g2==True:
                if green-step>=0:
                    green-=step
                else:
                    g2=False
                    r1=True
                    red+=step
            elif r1==True:
                if red+step<=255:
                    red+=step
                else:
                    r1=False
                    b2=True
                    blue-=step
            elif b2==True:
                if blue-step>=0:
                    blue-=step
                else:
                    b2=False
                    g1=True
                    green+=step
            colour.append((red,green,blue))
    else:
        for i in range(0,n):
            step=255//n
            colour.append((255-(step*i),0,step*i))

class ispis(object):
    
    def popunjavanje():
        global n
        global window
        global k
        for i in range (0,n):
            for j in range (0,n):
                if (i+j)%2==0:
                    pe.draw.rect(window,(255,255,255),(j*k,i*k,k,k))
                else:
                    pe.draw.rect(window,(0,0,0),(j*k,i*k,k,k))

    def  obelezavanje(x,y,c):
        global window
        global n
        global k
        global colour
        pe.draw.rect(window,colour[c],(x*k,y*k,k,k))
        
    def brisanje(x,y):
        global k
        global window
        if (x%2==0 and y%2==1)or(x%2==1 and y%2==0):
            pe.draw.rect(window,(0,0,0),(x*k,y*k,k,k))
        else:
            pe.draw.rect(window,(255,255,255),(x*k,y*k,k,k))

    def zavrsi():
        print("Nema resenja!!!")
        pe.quit()

def promena_prve_linije(string):
        f=open(string,"r")
        lines = f.readlines()
        f.close()

        f=open(string,"r")
        f.readline()
        n=int(f.readline())
        f.close()

        lines[1] = str(n+1) + '\n'
        
        f=open(string, "w")
        f.writelines(lines)
        f.close()

class fajlovi(object):

    def pravljenje(n, MPx, MPy):
        string="pozicija"+str(n)+".txt"
        f=open(string,'w')
        f.write(str(len(MPx))+"\n0\n")
        for i in range(0,len(MPx)):
            f.write(str(i)+'\n'+str(MPx[i])+'\n'+str(MPy[i])+'\n')
        f.close()

    def citanje(n):
        string="pozicija"+str(n)+".txt"
        f=open(string,'r')
        l=int(f.readline())
        if l==0:
            return False
        C=int(f.readline())
        promena_prve_linije(string)
        for i in range(0,l):
            c=int(f.readline())
            
            if c==C:
                x=int(f.readline())
                y=int(f.readline())
                return x,y
            else:
                f.readline()
                f.readline()
        return False

    def brisanje():
        global n
        for i in range(1,n+1):
            os.unlink("pozicija"+str(i)+".txt")