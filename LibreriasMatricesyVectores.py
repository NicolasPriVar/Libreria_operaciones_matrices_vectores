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
        #print(elemento)  
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
        #print(elemento)  
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
#Función principal
if __name__ == '__main__':
    print_hi('PyCharm')