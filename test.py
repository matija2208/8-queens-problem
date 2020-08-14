import numpy

def unos():
    return int(input('Unesite n : '))

def ispis(tabla):
    print(tabla)

def provera(tabla, x_sadasnje, y_sadasnje, n):

    for y_na_tabli in range(0, y_sadasnje):
        for x_na_tabli in range(0, n):
            if tabla[y_na_tabli][x_na_tabli] == 1:
                if x_na_tabli == x_sadasnje:
                    return False
                elif abs(y_na_tabli - y_sadasnje) == abs(x_na_tabli - x_sadasnje):
                    return False
    return True

def trazenje_mogucih_pozicija(tabla, R_broj_kraljice, R_broj_kombinacije, n):
    
    y = R_broj_kraljice
    counter = 0
    mogucnost = False
    for x in range(0,n):
        test=provera(tabla, x, y, n)
        if test:
            if counter == R_broj_kombinacije[R_broj_kraljice]:
                tabla[y][x] = 1
                mogucnost = True
                break
            elif counter < R_broj_kombinacije[R_broj_kraljice]:
                counter += 1
            else:
                break
    
    if mogucnost:
        if R_broj_kraljice == (n-1):
            return tabla
        else:
            R_broj_kraljice += 1
            R_broj_kombinacije[R_broj_kraljice] = 0
            return trazenje_mogucih_pozicija(tabla, R_broj_kraljice, R_broj_kombinacije, n)
    else:
        if R_broj_kraljice == 0:
            return None

        R_broj_kombinacije[R_broj_kraljice] = 0
        R_broj_kraljice -= 1
        R_broj_kombinacije[R_broj_kraljice] += 1

        y = R_broj_kraljice
        for x in range(0, n):        
            tabla[y][x] = 0

        return trazenje_mogucih_pozicija(tabla, R_broj_kraljice, R_broj_kombinacije, n)

def Algoritam():
    n = unos()
    tabla = [[0 for x in range(n)] for y in range(n)]
    R_broj_kraljice = 0
    R_broj_kombinacije = [0]*n
    tabla = trazenje_mogucih_pozicija(tabla, R_broj_kraljice, R_broj_kombinacije, n)

    if tabla == None:
        print('Nije moguce')
    else:
        tabla = numpy.reshape(tabla,(n,n))
        ispis(tabla)


Algoritam()