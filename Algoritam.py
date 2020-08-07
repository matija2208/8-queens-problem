import IO



n=IO.gui.inicijalizacija()
Qx=[0]*n
Qy=[0]*n
c=(-1)
bool=True

def trazenje_mogucih_pozicija(): 

    global n
    global Qx
    global Qy
    global c

    cu=0
    b=True
    Nx=[]
    Ny=[]
    y=c

    for x in range(0,n):
        for i in range(0,c):
                    
            if x == Qx[i] or y == Qy[i] or abs(y - Qy[i]) == abs(x - Qx[i]):
                b=False
                break
                
        if b==True:
            Nx.append(1)
            Nx[cu]=x
            Ny.append(1)
            Ny[cu]=y
            cu+=1
        else:
            b=True
        
    IO.fajlovi.pravljenje(c,Nx,Ny)

class Algoritam(object):

    def joshua():
        
        global n
        global Qx
        global Qy
        global c
        global bool
        if bool:
            if c==(-1):
                IO.inicijalizacija_boja()
                c=1
                Qx[0]=0
                Qy[0]=0
                IO.ispis.obelezavanje(Qx[0],Qy[0],0)
                trazenje_mogucih_pozicija()

            elif c==0:
                if Qx[0]==n-1:
                    IO.ispis.zavrsi()
                else:
                    Qx[0]+=1
                IO.ispis.obelezavanje(Qx[0],Qy[0],0)
                c=1
                trazenje_mogucih_pozicija()

            else:
                kordinate=IO.fajlovi.citanje(c)
        
                if kordinate==False:
                    IO.ispis.brisanje(Qx[c-1],Qy[c-1])
                    c-=1
            
                else:
                    Qx[c]=kordinate[0]
                    Qy[c]=kordinate[1]
                    IO.ispis.obelezavanje(Qx[c],Qy[c],c)
                    c+=1
                    trazenje_mogucih_pozicija()

                if c==n:
                    print("Resenje je pronadjeno!!!")
                    IO.fajlovi.brisanje()
                    bool=False