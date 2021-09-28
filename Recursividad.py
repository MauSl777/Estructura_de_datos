#sacar la suma de 1 al numero dado. si nos dan el 5, devolvera 5+4+3+2+1= 15
#tema general operaciones matematicas.
def sumaRecursividad(numero):

    if numero == 1:
        return 1
    else:
        return numero + sumaRecursividad(numero - 1)

print(sumaRecursividad(5))

#sacar el factorial de un numero.
def Factorial(numero):

    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero - 1)

print(Factorial(5))

#recorrer una lista de forma recursiva.
def mostrarListaRec(lista, indice):
    

    if indice != len(lista):
        print(lista[indice])
        mostrarListaRec(lista, indice + 1)

lista = [1,2,3,4,5,6,7,8,9]
mostrarListaRec(lista, 1 )

#1+1/2+1/3+1/4

def suma_harmonica(n):
     if n==1:
         resultado=1
     else:
        resultado=(1/n)+suma_harmonica(n-1)
     return resultado
print(suma_harmonica(5))

#calcular la potencia de un numero
def potencia(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * potencia(a, b -1)
        
print(potencia(2,4))
