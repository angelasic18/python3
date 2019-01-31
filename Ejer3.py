##angela

quetzal_dolar = 7.73
dolar_quetzal = 0.13
cantidad = 0
total = 0

print("Bienvenidos al convertidor".center(50,"-"))
opcion=input("¿quiere acceder al convertidor de dolares y quetzales?1-si 2-no:.")

while opcion != "2":
    if opcion == "1":
        pregunta = input("1.quetzales a dolares\n2.dolares a quetzales\n3.salir\ingrese su opcin:.")
        while pregunta != "3":
            if pregunta == "1":
                print("quetzaes a dolares".center(50,"-"))
                cantidad = float(input)("ingrese cantidad en dolares:.")
                total = cantidad*quetzal_dolar
                print("su total es:.Q.",total,"--valor del dolar en quetzales es:.Q.",quetzal_dolar)
            elif pregunta == "2":
                      print("dolares a quetzales".center(50,"-"))
                      cantidad = float(input("ingrese la cantidad en quetzales:."))
                      total = (cantidad*dolar_quetzal)
                      print("su total es:.$.",total,"--valor del quetzal en dolares es:.$.",dolar_quetzal)
            else:
                print("opcion incorreta... intente de nuevo conlas opciones disponibles")
            pregunta = input("1.quetzales a dolares\n2.dolares a quetzales\n3.salir\ingrese su opcion:.")
            if:
                print("ingrese -1- para acceder, -2- para salir... ingrese de nuevamente")
                opcion=input("¿quiere ingresar al convertidor de dolares y quetzales 1-si 2-no:.")
