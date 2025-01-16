Naranja_claro_aproximado = "\033[91m"
azul = "\033[34m"

from datetime import datetime
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class Hotel:
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, nom_hotel, telefono_hotel):
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.nom_hotel = nom_hotel
        self.telefono_hotel = telefono_hotel
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class DatosPersonales:
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, identificacion, nombre):
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.identificacion = identificacion
        self.nombre = nombre
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class Empleado(DatosPersonales):
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, cargo, identificacion, nombre, fecha_inicio, fecha_salida):
        super().__init__(identificacion, nombre)
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.cargo = cargo
        self.fecha_inicio = fecha_inicio
        self.fecha_salida = fecha_salida
    #Usamos class para definir un conjunto de métodos y atributos que describen un objeto
    #Usamos el def para definir una funcion de codigo reutilizable
    def atender_cliente(self, identificacion):
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        if self.identificacion == identificacion:
            #Usamos return para finalizar una función y devolver un valor calculado
            return ("")
        #Usamos else para  cuando la condición del "if" es evaluada como falsa
        else:
            return Naranja_claro_aproximado +"Identificación del empleado es incorrecta."
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class Cliente(DatosPersonales):
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, identificacion, nombre, telefono_cliente):
        super().__init__(identificacion, nombre)
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.telefono_cliente = telefono_cliente
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class Reservacion(Hotel):
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, num_reserva, num_personas, nom_hotel, telefono_hotel, saldo_habitacion_normal):
        super().__init__(nom_hotel, telefono_hotel)
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.numero_reserva = num_reserva
        self.num_personas = num_personas
        self.saldo_habitacion_normal = saldo_habitacion_normal
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class HabitacionEstandar:
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, num_per, capacidad, precio, disponibles=True, aire_acondicionado=True):
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.num_per = num_per
        self.capacidad = capacidad
        self.precio = precio
        self.disponibles = disponibles
        self.aire_acondicionado = aire_acondicionado
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class HabitacionNormal:
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, num_per, capacidad, precio, disponibles=True, ventilador=True):
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.num_per = num_per
        self.capacidad = capacidad
        self.precio = precio
        self.disponibles = disponibles
        self.ventilador = ventilador
        
salir = ""
#Usamos el while para crear una estructura repetitiva
while salir != "si":
    #Usaremos try para manejar excepciones o errores que pueden ocurrir durante la ejecución de un programa
    try:
        print(azul +"Bienvenido al Hotel, por favor llenemos las 3 primeras opciones en orden para que el programa se pueda ejecutar correctamente")
        print(Naranja_claro_aproximado +"""
        1) Empleados
        2) Cliente
        3) Reservas
        4) Habitacion estandar
        5) Habitacion normal
        6) cancelacion reservas
        7) Finalizar reserva
        """)
        opcion = int(input(azul +"Por favor eliga una de estas opciones: "))
        #Usamos el if para controlar el flujo de una condicion 
        if opcion == 1:
            print(Naranja_claro_aproximado +"Opción de empleados")
            nombre = input(azul+"Ingrese su nombre querido empleado: ")
            identificacion = int(input(azul+"Ingresa tu identificación querido empleado: "))
            cargo = input(azul+"Ingresa tu cargo: ")
            print(azul+"El empleado que seleccionaste es", nombre, "con una identificacion de", identificacion,"su cargo es", cargo,"y sera quien te antendera de aqui en adelnate")
            print(azul+"Por favor querido cliente llenemos esta solicitud de fechas ")
            datetime
            fecha_inicio = input(azul+"Ingresa la fecha de inicio (DD/MM/YYYY): ")
            fecha_salida = input(azul+"Ingresa la fecha final (DD/MM/YYYY): ")
            if fecha_salida >= fecha_inicio:
                print(Naranja_claro_aproximado+"La fecha de inicio del usuario es desde el dia", fecha_inicio, "hasta el dia", fecha_salida)
            else:
                print(azul+"Error ingresa fechas validas")
            empleado = Empleado(cargo, identificacion, nombre, fecha_inicio, fecha_salida)

        elif opcion ==2:
            print(Naranja_claro_aproximado +"Estas en la opcion de clientes: ")
            nom_cliente = input(azul +"Ingresa tu nombre querido cliente: ")
            tel_cliente = int(input(azul +"Ingresa tu numero de telefono: "))
            identificacion = int(input(azul+"Querido cliente ingresa el numero de tu identificacion: "))
            cliente = Cliente(nom_cliente, identificacion, tel_cliente,)
            
        elif opcion ==3:
            print(Naranja_claro_aproximado +"Estas en la opcion de reservas")
            nom = print (azul +"El nombre del hotel es Greet")
            tele_hotel = print(azul +"El numero del hotel es +57 3214997981")
            nu_reserva = input( azul +"Tu numero de reserva es: " )
            nu_personas = input(azul +"Ingresa el numero de personas: ")
            saldo_habitacion_normal = None
            print(Naranja_claro_aproximado +"Querido", nom_cliente,"su numero de telefono es",  tel_cliente, "su identificacion es", identificacion," y tomamos sus datos personales de la informacion de clientes")
            reserva = Reservacion(nu_reserva, nu_personas, nom, None, tele_hotel)
            
        elif opcion == 4:
            print(Naranja_claro_aproximado +"Estás en la opción de habitación estándar")
            capacidad_maxima = 6
            num_personas = int(input(azul +"Ingresa el número de personas: "))
            #Usamos el if para controlar el flujo de una condicion 
            if num_personas <= capacidad_maxima:
                precio = 320000
                aire = 20000
                total = precio + aire
                precio += aire
                print(Naranja_claro_aproximado +"""Nuestras habitaciones estandar ofrecen esto:
                * 3 Somieres con su respectivo espaldar
                * Un baño amplio
                * Aire acondicionado
                * TV
                * Un escritorio
                * Wifi
                * Un armario con perchas
                * calefacción individual
                * Y limpieza
                """)
                print(azul +"El precio de las habitaciones estándar es de un total de", total, "pesos")

                per = ""
                #Usamos el if para controlar el flujo de una condicion 
                if per != "si":
                    per = input(Naranja_claro_aproximado +"""Deseas hacer la reservación
                    1) si
                    2) no
                    """)
                    #Usamos el if para controlar el flujo de una condicion 
                    if per == azul+"si":
                        print(azul +"La habitación es tuya, querido usuario")
                    #Usamos el if para controlar el flujo de una condicion 
                    if per == azul+"no":
                        print(azul+"Ok, entendemos que no deseas esta habitación...")
            else:
                print(azul +"Lo sentimos, la capacidad máxima de una habitación estándar es de", capacidad_maxima, "personas")

        elif opcion == 5:
            print(Naranja_claro_aproximado +"Estás en el opción de habitaciones normales")
            capa_maxima = 3
            num_personas = int(input(azul +"Ingresa el número de personas: "))
            print(Naranja_claro_aproximado +"""Nuestras habitaciones estandar ofrecen esto:
            * 2 camas individuales
            * Mobiliario básico 
            * Un baño
            * Un ventilador
            * Limpieza
            """)
            #Usamos el if para controlar el flujo de una condicion 
            if num_personas <= capa_maxima:
                precios = 120000
                print("El precio de las habitaciones normales es de un total de", precios, "pesos")

                per = ""
                #Usamos el if para controlar el flujo de una condicion 
                if per != "si":
                    per = input(Naranja_claro_aproximado +"""Deseas hacer la reservación de la habitación normal
                    1) si
                    2) no
                    """)
                    #Usamos el if para controlar el flujo de una condicion 
                    if per == azul +"si":
                        print(azul +"La habitación normal es tuya, querido usuario")
                    #Usamos el if para controlar el flujo de una condicion 
                    if per == azul +"no":
                        print(azul +"Ok, entendemos que no deseas esta habitación...")
            #Usamos else para  cuando la condición del "if" es evaluada como falsa
            else:
                print(azul+"La capacidad máxima de las habitaciones normales es de 3 personas")
        
        elif opcion == 6:
            print(Naranja_claro_aproximado +"Estás en la opción de cancelar reservas")

            confirmar = input(Naranja_claro_aproximado +"""Estás seguro de cancelar la reserva?
            1) si
            2) no
            """)
            #Usamos el if para controlar el flujo de una condicion 
            if confirmar == "si":
                print(Naranja_claro_aproximado +"La revervacion que hizo anteriormente con el numero de reserva",nu_reserva,"el numero de peronas que son", num_personas, "mas la fecha de inicio que es desde el dia", fecha_inicio,"y la fecha de salida que es desde el dia", fecha_salida, "han sido canceladas exitosamente")

            elif confirmar == "no":
                print(azul +"Cancelación de reserva cancelada ")

        elif opcion == 7:
            salir=input(Naranja_claro_aproximado +"""Deseas salir del programa?
            1) si
            2) no
            """)
            #Usamos el if para controlar el flujo de una condicion       
            if salir == "si":
                print(azul +"Saliste del programa")
                break
            #Usamos el if para controlar el flujo de una condicion 
            if salir =="no":
                print(azul +"Volviendo al menu.....")
            #Usamos else para  cuando la condición del "if" es evaluada como falsa
            else:
                print(azul +"Opción inválida. Por favor, seleccione un número válido.")
    #Usamos el except para  tratar posibles errores que ocurren durante la ejecución de un programa
    except:
        print(Naranja_claro_aproximado +"Error por favor dijite solo lo que piden")