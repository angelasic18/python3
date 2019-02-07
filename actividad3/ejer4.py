#ejercicio4
#realizar el promedio de N notas utilizando el for

print("Bienvenidos al programa".center(50,"*"))
N= 0
suma = 0
print("ingrese notas que desee pulsar 1.para detener")
cantidad = int(input("ingrese la camntidad de notas"))
for i in range (notas):
    N = int(input("ingrese la notas:."))
    suma = suma + N
promedio = suma / notas
print("el promedio es:. {}".format(promedio))
                                       
