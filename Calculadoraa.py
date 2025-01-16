print("Querido usuario por favor solo selecione 1 de las 7 opciones que estan en el menu principal")
print("menu principal")
eleccion =0
while eleccion != 8:
    print ("""
    1) calculadora 
    2) convertir distancia
    3) convertir masa
    4) area y perimetro de un circulo
    5) ingresar N notas de una materia
    6) numeros primos de un numero
    7) salir """)
    eleccion =int(input())
# Calculadora
    if eleccion == 1:
        print(" seleccionaste la calculadora")
        print("Digite un numero que no sea 0 para que la division no tenga error")
        numero1=int(input("Ingrese el primer numero: "))
        numero2=int(input("Ingresa el segundo numero: "))
        opcion = 0
        
        while opcion != 5:
            print("""
            1) suma
            2) resta
            3) multiplicacion
            4) division 
            5) salir""")
            opcion = int(input())

            if opcion == 1:
                print(" ")
                print("el resultado de la suma", numero1, "+", numero2, "es =", numero1+numero2)

            elif opcion == 2:
                print(" ")
                print("el resultado de la resta", numero1, "-", numero2, "es =", numero1-numero2)
                
            elif opcion == 3:
                print(" ")
                print("el resultado de la multiplicacion", numero1, "*", numero2, "es =", numero1*numero2)
                
            elif opcion == 4:
                print(" ")
                print("el resultado de la division", numero1, "/", numero2, "es =", numero1/numero2)
                
            elif opcion == 5:
                print("estas en el menu princupal")
                break
            else:
                print("opcion invalida, por favor intente nuevamente")
# convertidor de distancia         
    elif eleccion == 2:
        print("selecionaste el convertidor de distancia")
        print("Selecione el convertidor de distancia que deseas usar")
        opcion = 0

        while opcion != 5:
            print("""
            1) kilometros a metros
            2) metros a kilometros
            3) kilometros a millas
            4) millas a kilometros
            5) salir """)
            opcion = int(input())

            if opcion == 1:
                kilometros = float(input("ingrese los kilometros que deseas convertir a metros: "))
                print(" ") 
                print("el resultado de kilometros a metros es =", kilometros * 1000, "metros" )

            elif opcion == 2:
                metros = float(input("ingrese los metros que deseas converit a kilometros: "))
                print(" ")
                print("el resultado de metros a kilometros es =", (metros * 1) / 10000, "kilometros")

            elif opcion == 3:
                kilometros1 = float(input("ingrese los kilometros que deseas convertir a millas: "))
                print(" ")
                print("el resultado de kilometros a millas es =", kilometros1 * 1.609, "millas")

            elif opcion ==4:
                millas= float(input("ingrese las millas que deseas convertir a kilometros: "))
                print(" ")
                print("el resultado de millas a kilometros es =",millas * 1.609, "kilometros")

            elif opcion == 5:
                print("estas en el menu princupal")
                break
            else:
                print("opcion invalida, por favor intente nuevamente")
# convertidor de masa
    if eleccion == 3:
        print("seleccionaste el convertidor de masa")
        print("selecione el convertidor de masa que deseas usar")
        opcion = 0

        while opcion != 5:
            print("""
            1) kilogramos a libras
            2) libras a kilogramos
            3) libras a gramos
            4) gramos a libras
            5) salir""")
            opcion = float(input())

            if opcion == 1:
                kilogramos =float(input("ingrese los kilogramos que desea convertir a libras: "))
                print(" ")
                print("el resultado de kilogramos a libras es =", kilogramos  * 2.205, "libras")

            elif opcion == 2:
                libras= float(input("ingrese las libras que desea convertir a kilogramos: "))
                print(" ")
                print("el resultado de libras a kilogramos es =", libras * 2.205, "kilogramos")

            elif opcion == 3:
                libras1= float(input("ingrese las libras que desea convertir a gramos: "))
                print(" ")
                print("el resultado de libras a gramos es =", libras1 * 453.6, "gramos")

            elif opcion == 4:
                gramos = float(input("ingrese los gramos que desea convertir a libras: "))
                print(" ")
                print("el resultado de gramos a libras es =", gramos * 453.6, "libras")

            elif opcion == 5:
                print("estas en el menu principal")
                break
            else:
                print("opcion invalida, por favor intente nuevamente")
# convertidor de area y perimetro de un circulo
    if eleccion == 4:
        print("seleccionaste el convertidor de area y perimetro de un circulo")
        opcion = 0

        while opcion != 2:
            print("""
            1) seleciona 1 para el area y perimetro de un circulo
            2) seleciona 2 para salir""")
            opcion = int(input())
            
            if opcion == 1:
                radio = float(input("ingrese el radio del circulo: "))
                area = 3.14159 * radio ** 2
                perimetro = 2 * 3.14159 * radio

                print("el area del circulo es: ", area)
                print("el perimetro del circulo es: ", perimetro)
            elif opcion == 2:
                print("esta en el menu principal")
                break
            else:
                print("opcion invalida, por favor intente nuevamente")
# convertidor de notas y promedio
    elif eleccion == 5:
        print("selecionaste el convertidor de notas y promedio")
        opcion = 0

        while opcion != 2:
            print("""
            1) seleciona 1 para las notas y el promedio
            2) salir""")
            opcion = int(input())
            suma=0
            if opcion == 1:
                Nnotas = int(input("ingresa la cantidad de notas"))
                for i in range(Nnotas):
                    notas = float(input(f"ingresa la nota {i + 1}: "))
                    suma = notas+suma
                    promedio = suma / Nnotas
                print("Su promedio es: ",promedio)
            elif opcion == 2:
                    print("estas en el meu principal")
                    break
            else:
                print("opcion invalida, por favor intente nuevamente")
# convertidor de los numeros primos
    elif eleccion == 6:
        print("selecionaste el convertidor de los numeros primos")
        opcion = 0
        
        while opcion != 2:

            print("""
            1) seleciona 1 para los numeros primos
            2) seleciona 2 para salir """)
            opcion = int(input())
            
            if opcion == 1:
                numero = int(input("Ingrese un número entero positivo: "))
                if numero <= 1:
                    print("El número debe ser mayor que 1: ")
                else:
                    primos = [2] # Inicializamos la lista de números primos con el primer número primo, 2.
                    for i in range(3, numero+1, 2):
                        if all(i % j != 0 for j in range(3, int(i**0.5) + 1, 2)):
                            primos.append(i)
                    print("Los números primos hasta", numero, "son:", primos)
            elif opcion == 2:
                print("estas en el menu principal")
                break
            else:
                print("opcion invalida, por favor intente nuevamente")
# Salida del programa              
    if eleccion == 7:
        salir= int(input("""Quieres salir del programa?
        8 para continuar
        0 para salir
        """))
        if salir ==0:
            print("saliste del programa :)")
            break
