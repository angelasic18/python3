##Angela
##calcular la eda actual de una persona,
##prevamente ingreso
##el año actual y el año de nacimiento
print("Bienvenidos al programa".center(50,"*"))
FEC_ACT = 2019
fec_nac = int(input("ingresa tu año de nacimiento"))

edad = FEC_ACT - fec_nac

print("tu edad es {}".format(edad))
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
