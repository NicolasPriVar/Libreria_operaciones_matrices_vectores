import  numpy as np
def print_hi(name):
    print(f'Hi, {name}')
#Suma de vectores
def SumVec(c,d):
    v=[]
    for i in range(len(c)):
         v.append(c[i]+d[i])
    return v
#Resta de vectores
def ResVec(c,d):
    v=[]
    for i in range(len(c)):
         v.append(c[i]-d[i])
    return v
#Multiplicación de un escalar por un vector complejo
def mulVec(c,e):
    v=[]
    for i in range(len(c)):
        v.append(e*c[i])
    return v
#Suma de matrices
def SumMat(a,b):
    ma=len(a)
    mb=len(b)
    na=(len(a[0]))
    nb=(len(b[0]))
    c=[[0 for i in range (len(a))]for j in range (len(b))]
    for elemento in c:
            if ma==mb and na==nb:
                for i in range (ma):
                    for j in range(na):
                        c[i][j]=a[i][j]+b[i][j]
                #print(elemento)  
    return c
#Resta de matrices
def ResMat(a,b):
    ma=len(a)
    mb=len(b)
    na=(len(a[0]))
    nb=(len(b[0]))
    c=[[0 for i in range (len(a))]for j in range (len(b))]
    for elemento in c:
            if ma==mb and na==nb:
                for i in range (ma):
                    for j in range(na):
                        c[i][j]=a[i][j]-b[i][j]
                #print(elemento)  
    return c
#Multiplicacioón de un escalar por una matriz compleja
def mulMat(a,e):
    ma=len(a)
    na=(len(a[0]))
    c=[[0 for i in range (len(a))]for j in range (len(a))]
    for elemento in c:
        for i in range (ma):
            for j in range(na):
                c[i][j]=e*a[i][j]
    return c
#Transpuesta de un vector complejo
def transpuestaVec(c):
    t=np.transpose(c)
    return t
#Transpuesta de una matriz compleja
def transpuestaMat(a):
    ma=len(a)
    na=(len(a[0]))
    c=[[0 for i in range (len(a))]for j in range (len(a))]
    for elemento in c:
        for i in range (ma):
            for j in range(na):
                c[i][j]=a[j][i]
    return c
#Conjugado de un vector
def conVec(c):
    for i in range(len(c)):
        c[i]=np.conj(c[i])
    return c
#Conjugado de una matriz
def conMat(a):    
    for i in range(len(a)):
        for j in range(len(a)):
            a[i][j]=np.conj(a[i][j])
    return(a)
#Adjunta de un vector
def dagaVector(c):
    t=np.transpose(c)
    for i in range (len(t)):
        c[i]=np.conj(c[i])
    return c
#Adjnta de una matriz
def dagaMatriz(a):
    ma=len(a)
    na=(len(a[0]))
    c=[[0 for i in range (len(a))]for j in range (len(a))]
    for elemento in c:
        for i in range (ma):
            for j in range(na):
                c[i][j]=np.conjugate(a[j][i])
    return c
#Multiplicación de matrices
def multiMatrices(a,b):
    tfa = len(a)
    tca = len(a[0])
    tfb = len(b)
    tcb = len(b[0])
    if tfa != tfb:
        print("Tamaños incompatibles")
    else:
        mult = [[0 for i in range (len(a))]for j in range (len(b))]
        for j in range(tfa):
            for k in range(tcb):
                for l in range(tfb):
                    mult[j][k] += a[j][l] * b[l][k]
    return(mult)
#Acción de una matriz sobre un vector
def accionMatVec(b,d):
    tfa = len(b)
    tca = len(b[0])
    tv = len(d)
    resultado = [[0 for i in range (len(b)-1)]for j in range (len(d))]
    for j in range(tv):
        for k in range(tca-1):
            for l in range(tfa):
                resultado[j][k] += b[j][l] * d[l]
    return resultado 
#Producto interno de dos vectores
def productoInterno(c,d):
    s=dagaVector(c)
    pi=0
    for i in range(len(c)):
        pi+=s[i]*d[i]
    return pi
#Norma de un vector
def normaVec(d):
    resultado = ((productoInterno(d,d))**(1/2))
    return resultado
#Distancia entre vectores
def distaciasVectores(c,d):
    p1=ResVec(c,d)
    resultado = (productoInterno(p1,p1))**(1/2)
    return resultado
#Valores propios de una matriz
def valoresMatriz(a):
    print(a)
#Matriz unitaria
def matrizUnitaria(a):
    if multiMatrices(a,dagaMatriz(a))==multiMatrices(dagaMatriz(a),a):
        b="Si es unitaria"
    else:
        b="No es unitaria"
    return b
#Matriz hermitiana
def matrizHermitiana(a):
    if a==dagaMatriz(a):
        b="Sí es hermitiana"
    else:
        b="No es hermitiana"
    return b
#Producto tensor de dos vectores
def productoTensorV(c,d):
    resultado=[]
    for i in range (len(c)):
        for j in range(len(d)):
            r=c[i]*d[j]
            resultado.append(r)
    return resultado
#Producto tensor de dos matrices
def productoTensorM(a,b):   
    n=len(b)
    n2=len(b[0])
    m=len(a)
    m2=len(a[0])
    t=n*m
    t2=n2*m2
    r=[[0 for i in range (t)]for j in range (t2)]
    for elemento in r:
        for i in range(t2):
            for j in range(t):
                r[i][j]=a[i//n][j//n2]*b[i%n][j%n2]
        print(elemento)
    return r

if __name__ == '__main__':
    
   print_hi('PyCharm')
