#ejercicio3
#realizar el primedio de 5 notas utilizando el siglo for

print("Bienvenidos al programa".center(50,"*"))
suma = 0
valor = 0
for i in range (5):
    N = int(input("ingrese N:."))
    suma = suma + N
    promedio = suma / 5
print("el promedio es:. {}".format(promedio))
