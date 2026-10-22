import numpy as np   
# catherine eileen huerta rascon NC = 0072
# ejemplos de numpy Numerical python
print("---------espaciado linealmente en arrayy ---------0072")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)

print("---------matriz identidad en 2D array ---------0072")
matriz=np.eye(3)
print(matriz)

print("---------generara numeros al azar en 2D array ---------0072")
numale=np.random.random((3,4)) # genera 12 numeros al azar
print(numale)

print("genera 9 numeros al azar entre 0 y 1")
numale=np.random.random((3,3)) # genera 12 numeros al azar
print(numale)

# como genera 9 números aleatorios comprendidos entre 1 y 20 con numpy en un arreglo de 3 por 3 
print("genera 9 números aleatorios comprendidos entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3,3)
print(arre)
print("catherine eileen huerta rascon NC = 0072")