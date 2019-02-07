#ejrcicio1
#solicitar al usuario que seleccione una
#opcion1 solicitar dos numero y elevar
#el primer numero elevado al segundo numero.
#opcion2 solicitar 3 numero y elevar el primero al segundo numero y el resultado
#elevarlo al tercero
elevacion = 0
print("Bienvendios".center(18,"*"))
opcion=input("1.dos nuemro elevar el primer numero elevando al segundo numero 2. 3 numeros elevar el primero al segundo nuemro y el resultado elevarlo al tercero:.")

if opcion == "1":
    valor1 = input("ingrese el primer numero")
    valor2 = input("ingrese el sengundo numero")
    elevacion = int(valor1) ** int(valor2)
    print("la elevacion es:. {}".format(elevacion))
elif opcion == "2":
    valor1 = int(input("ingrese primer valor"))
    valor2 = int(input("ingresa segundo valor"))
    valor3 = int(input("ingrese tercer valor"))
    elevacion = (valor1 ** valor2) ** valor3
    print("la elevacion es:. {}".format(elevacion))
else:
    ("opcion no valida")
    
