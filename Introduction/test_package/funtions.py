# Funtions

# Create a funtions
def sayHellow(): # Define la funcion
    print('Hello')
    
sayHellow() # Declara la funcion

# Create a funtions
def sayHello(name = 'default'): # Define la funcion y un parametro pero con un valor predeterminado
    print('Hello', name)
    'Texto invisible'
    
sayHello('Arturo') # Declara la funcion


# Retornar un valor
def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(2, 2)
print(numSum)

# Los valores se alteran solo dentro de la funcion
valor = 1

def addOne(num):
    num = 15
    print('Value inside  function: ', num)
    return

addOne(valor)
print('Value outside function: ', valor)


# Las listas contienen valores mutables
lista = [1,2,3]

def addOneList(lista):
    lista.append(4)
    print('Value inside function',lista)
    return

addOneList(lista)
print('Value outside function: ',lista)