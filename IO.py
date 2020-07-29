import pygame as pe
import pygamebg as pg

n=1
window=0


def unos():
    global n
    n=int(input("Unesite broj n : "))
    return n

class ispis(object):
    
    def inicijalizacija():
        global n
        global window
        window=pg.open_window(n*50,n*50,"Tabla")
        
    
    def popunjavanje():
        global n
        global window
        for i in range (0,n):
            for j in range (0,n):
                if (i+j)%2==0:
                    pe.draw.rect(window,(255,255,255),(j*50,i*50,50,50))
                else:
                    pe.draw.rect(window,(0,0,0),(j*50,i*50,50,50))
        

    def  obelezavanje(x,y,c):
        global window
        global n
        step=255/n
        pe.draw.rect(window,(255,0,0),(x*50,y*50,50,50))
        
    
    def zavrsi():
        print("Nema resenja!!!")
        quit()
    
    def brisanje(x,y):
        if (x%2==0 and y%2==1)or(x%2==1 and y%2==0):
            pe.draw.rect(window,(0,0,0),(x*50,y*50,50,50))
        else:
            pe.draw.rect(window,(255,255,255),(x*50,y*50,50,50))

    def kraj():
        print("kraj!!!")
        pg.wait_loop()

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