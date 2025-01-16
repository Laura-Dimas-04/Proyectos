from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import simpledialog, messagebox
#Usamos el def para definir una funcion de codigo reutilizable
def convertir_pesos():
    #Usaremos try para manejar excepciones o errores que pueden ocurrir durante la ejecución de un programa
    try:
        #Usaremos simpledialog para crear cuadros de diálogo en aplicaciones gráficas.
        #Usaremos askinteger para mostrar un cuadro de diálogo que solicita al usuario ingresar un número entero.
        pesos = simpledialog.askinteger("Conversión de Pesos a Dólares", "Ingresa la cantidad de dinero en pesos: ")
        #Usaremos float para representar números decimales
        pesos = float(pesos)
        interes = 4.066
        #Usaremos round para redondear un número a una cantidad específica de dígitos decimales
        pesos_convertidos = round(pesos / interes, 2)
        mensaje = f"Querido cliente, la cantidad ingresada en pesos que es de {pesos} pesos colombianos equivale a ${pesos_convertidos} dólares"
        #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas.
        #Usaremos showinfo para mostrar un cuadro de diálogo de información.
        messagebox.showinfo("Resultado de la conversión", mensaje)
    #Usamos el except para  tratar posibles errores que ocurren durante la ejecución de un programa
    except (TypeError, ValueError):
        #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas
        #Usamos showwarning para mostrar un cuadro de diálogo de advertencia.
        messagebox.showwarning("Error", "Por favor, ingresa valores numéricos válidos")
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class Banco:
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, nombre):
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.nombre = nombre

#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class Cliente(Banco):
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, nombre, numero_identificacion, contraseña, saldos=100000):
        super().__init__(nombre)
        #Usaremos self. para hacer referencia al objeto que se está manipulando
        self.numero_identificacion = numero_identificacion
        self.contraseña = contraseña
        self.saldos = saldos
    #Usamos el def para definir una funcion de codigo reutilizable
    def tipo(self, operacion, monto, numero_identificacion, contraseña):
        #Usamos el if para controlar el flujo de una condicion 
        if operacion == "deposito":
            self.saldos += monto
            #Usaremos return para devolver un valor específico al punto de llamada de la función.
            return f"Querido usuario, has depositado {monto} pesos en tu cuenta y tienes un total de {self.saldos} pesos en tu cuenta bancaria."
        #Usaremos elif para comprobar múltiples condiciones después de que una condición "if" resulta ser falsa.
        elif operacion == "retiro":
            #Usamos el if para controlar el flujo de una condicion 
            if numero_identificacion == self.numero_identificacion and contraseña == self.contraseña:
                #Usamos el if para controlar el flujo de una condicion 
                if monto <= self.saldos:
                    self.saldos -= monto
                    #Usaremos return para devolver un valor específico al punto de llamada de la función.
                    return f"Retiro realizado con éxito, tu saldo actual es de {self.saldos} pesos."
                #Usamos else para  cuando la condición del "if" es evaluada como falsa
                else:
                    #Usaremos return para devolver un valor específico al punto de llamada de la función.
                    return "Saldo insuficiente. No se puede realizar el retiro."
            #Usaremos elif para comprobar múltiples condiciones después de que una condición "if" resulta ser falsa.
            elif numero_identificacion != self.numero_identificacion:
                #Usaremos return para devolver un valor específico al punto de llamada de la función.
                return "Identificación incorrecta. No se puede realizar la operación."
            #Usaremos elif para comprobar múltiples condiciones después de que una condición "if" resulta ser falsa.
            elif contraseña != self.contraseña:
                #Usaremos return para devolver un valor específico al punto de llamada de la función.
                return "Contraseña incorrecta."
    
#Usaremos Tk para crear una instancia de la clase Tk, que representa la ventana principal de una interfaz gráfica 
aplicacion = Tk()
#Usaremos geometry para establecer las dimensiones iniciales y la posición de la ventana principal de una aplicación gráfica.
aplicacion.geometry("1250x680+130+60")
#Usaremos title para establecer el título de la ventana principal
aplicacion.title("Bancos internacionales")
#Usaremos config para configurar las opciones de un widget
#Usaremos bg para establecer el color de fondo de un widget
aplicacion.config(bg="gray1")

#Usaremos Frame para contener y organizar otros widgets.
#Usaremos relief para especificar el tipo de borde que rodea un widget
#Usaremos FLAT El valor "flat" para la opción relief en Tkinter se utiliza para especificar que el widget no tendrá ningún relieve en su borde.
#Usaremos bg para establecer el color de fondo de un widget
#Usaremos width para especificar el ancho de un widget
#Usaremos height para especificar la altura de un widget
ventana = Frame(aplicacion, relief=FLAT, bg="white", width=500, height=200)
#Usaremos pack  para organizar y colocar un widget dentro de su contenedor principal
#Usaremos side="right" side="right" con el método pack(), estás indicando que deseas colocar el widget en el lado derecho del contenedor.
#Usaremos padx para especificar el espacio de relleno horizontal alrededor de un widget.
#Usaremos pady para especificar el espacio de relleno vertical alrededor de un widget.
#Usaremos expand=True Cuando usas el parámetro expand=True junto con el método pack() estás indicando que el widget debe expandirse para ocupar cualquier espacio adicional disponible en la dirección especificada por la opción side
ventana.pack(side="right", padx=30, pady=0, expand=True)
#Usaremos Frame para contener y organizar otros widgets.
#Usaremos relief para especificar el tipo de borde que rodea un widget
#Usaremos FLAT El valor "flat" para la opción relief en Tkinter se utiliza para especificar que el widget no tendrá ningún relieve en su borde.
#Usaremos bg para establecer el color de fondo de un widget
#Usaremos width para especificar el ancho de un widget
#Usaremos height para especificar la altura de un widget
ventana2 = Frame(ventana, relief="flat", bg="gray1", width=350, height=300)
#Usaremos pack  para organizar y colocar un widget dentro de su contenedor principal
#Usaremos side="right" side="right" con el método pack(), estás indicando que deseas colocar el widget en el lado derecho del contenedor.
#Usaremos padx para especificar el espacio de relleno horizontal alrededor de un widget.
#Usaremos pady para especificar el espacio de relleno vertical alrededor de un widget.
#Usaremos expand=True Cuando usas el parámetro expand=True junto con el método pack() estás indicando que el widget debe expandirse para ocupar cualquier espacio adicional disponible en la dirección especificada por la opción side
ventana.pack(side="right", padx=30, pady=0, expand=True)
ventana2.pack(side="top", padx=10, pady=10, expand=True, fill="both")
#Usaremos pack  para organizar y colocar un widget dentro de su contenedor principal
#Usaremos side="top" Cuando utilizas side="top" junto con el método pack() en Tkinter, estás indicando que deseas colocar el widget en la parte superior del contenedor.
#Usaremos padx para especificar el espacio de relleno horizontal alrededor de un widget.
#Usaremos pady para especificar el espacio de relleno vertical alrededor de un widget.
#Usaremos expand=True Cuando usas el parámetro expand=True junto con el método pack() estás indicando que el widget debe expandirse para ocupar cualquier espacio adicional disponible en la dirección especificada por la opción side
#Usaremos fill="both" Cuando utilizas fill="both" junto con el método pack() estás indicando que deseas que el widget se expanda tanto en la dirección horizontal como en la vertical para ocupar todo el espacio disponible
ventana.pack(side="right", padx=30, pady=0, expand=True)
#Usaremos pack  para organizar y colocar un widget dentro de su contenedor principal
#Usaremos side="right" side="right" con el método pack(), estás indicando que deseas colocar el widget en el lado derecho del contenedor.
#Usaremos padx para especificar el espacio de relleno horizontal alrededor de un widget.
#Usaremos pady para especificar el espacio de relleno vertical alrededor de un widget.
#Usaremos expand=True Cuando usas el parámetro expand=True junto con el método pack() estás indicando que el widget debe expandirse para ocupar cualquier espacio adicional disponible en la dirección especificada por la opción side

#Usamoa Label  para mostrar texto o imágenes en una interfaz
titulo3 = Label(ventana2, text="Bienvenido, estamos aquí para ayudarte en el proceso de conversión de pesos a dólares. Para realizar esta operación, simplemente da click en el botón que aparece en pantalla como Convertir a pesos",
                fg="black", font=("Bell MT", 13), wraplength=280, bg="white")
titulo3.place(relx=0.1, rely=0.1)

#Usaremos Button para crear botones en una interfaz gráfica.
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
boton = Button(ventana2, text="¿Deseas convertir a pesos?", command=convertir_pesos, pady=10, padx=35)
boton.place(relx=0.2, rely=0.6)

#Usamos Image.open para abrir y cargar una imagen desde un archivo.
#Usamos  ImageTk.PhotoImage para convertir imágenes abiertas con Image.open 
imageness = Image.open("sistema-bancario.jpg")
tamaños = (100, 100)
redi = imageness.resize(tamaños)
imagen = ImageTk.PhotoImage(redi)


#Usamoa Label  para mostrar texto o imágenes en una interfaz
#Usaremos Frame para contener y organizar otros widgets.
panel_superior = Frame(aplicacion, relief=FLAT, bg="gray1")
panel_superior.pack(side="top", padx=30, pady=0, anchor="w")
titulo_imagen = Label(panel_superior, image=imagen)
titulo_imagen.pack(side="left", padx=10, pady=10)
titulo = Label(panel_superior, text="Bancos internacionales", fg="light yellow", font=("Bell MT", 40), bg="gray1")
titulo.pack(side="left", padx=50, pady=10, anchor="w")
panel_abajo = Frame(aplicacion, relief=FLAT)
panel_abajo.pack(side="bottom", padx=50, pady=30, anchor="nw")
titulo2 = Label(panel_abajo, text="Gracias por depositar tu confianza en nuestras manos!", fg="light yellow", font=("Bell MT", 20), bg="gray1", width=40, anchor="nw")
titulo2.pack(side="left", padx=0, pady=0)

#Usamos el def para definir una funcion de codigo reutilizable
#Usamos random para la generación de números pseudoaleatorios
#Usamos randint que genera un número entero aleatorio entre los valores
def crear_estrella():
    x = random.randint(0, ancho)
    y = random.randint(0, alto)
    tamaño = random.randint(1, 3)
    lienzo.create_oval(x, y, x + tamaño, y + tamaño, fill="white", outline="white")
#Usamos el def para definir una funcion de codigo reutilizable
def generar_estrellas(event):
    for _ in range(5):
        crear_estrella()

#Usamos winfo_screenwidth para obtener el ancho de la pantalla en píxeles
#Usamos canvas para crear un área de dibujo en la que puedes realizar dibujos y mostrar imágenes
#Usamos highlightthickness para especificar el grosor del resaltado de la entrada 
#Usamos fill=BOTH para indicar que el widget debe expandirse tanto horizontal como verticalmente
#Usamos expand=YES para indicar si un widget debe expandirse para ocupar el espacio disponible en su contenedor
ancho = aplicacion.winfo_screenwidth()
alto = aplicacion.winfo_screenheight()
lienzo = Canvas(aplicacion, width=ancho, height=alto, bg="gray1", highlightthickness=0)
lienzo.pack(fill=BOTH, expand=YES)

#Usamos bind para definir qué acción debe realizarse cuando ocurre un evento específico, como hacer clic en un botón, presionar una tecla, o mover el ratón sobre un widget
#Usamos "<Motion>" para un evento que se activa cada vez que el ratón se mueve dentro de los límites del widget al que está asociado.
aplicacion.bind("<Motion>", generar_estrellas)

#Usamos Entry para crear un campo de entrada de una sola línea que permite al usuario ingresar texto.
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
#Usamoa Label  para mostrar texto o imágenes en una interfaz
#Usaremos text  para establecer el texto en el botón 
entry_nombre = Entry(aplicacion)
entry_nombre.place(relx=0.4, rely=0.3)
Caja1 = Label(aplicacion, text="Ingresa tu nombre: ", font=("Bell MT", 12), fg="purple")
Caja1.place(relx=0.1, rely=0.3, anchor="w")

#Usamos Entry para crear un campo de entrada de una sola línea que permite al usuario ingresar texto.
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
#Usamoa Label  para mostrar texto o imágenes en una interfaz
#Usaremos text  para establecer el texto en el botón 
entry_identificacion = Entry(aplicacion)
entry_identificacion.place(relx=0.4, rely=0.4, anchor="w")
Caja3 = Label(aplicacion, text="Ingresa el numero de identificación: ", fg="purple", font=("Bell MT", 12))
Caja3.place(relx=0.1, rely=0.4, anchor="w")

#Usamos Entry para crear un campo de entrada de una sola línea que permite al usuario ingresar texto.
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
#Usamoa Label  para mostrar texto o imágenes en una interfaz
#Usaremos text  para establecer el texto en el botón 
entry_conta = Entry(aplicacion, show="*")
entry_conta.place(relx=0.4, rely=0.5,)
Caja4 = Label(aplicacion, text="Ingresa la contraseña: ", fg="purple", font=("Bell MT", 12))
Caja4.place(relx=0.1, rely=0.5)
#Usamos class para definir un conjunto de métodos y atributos que describen un objeto
class tex:
    #Usamos el def para definir una funcion de codigo reutilizable
    def __init__(self, orin):
        self.orin = orin
        orin.title("Estás en la ventana de depósitos y retiros")

        self.entry_nombre = entry_nombre
        self.entry_identificacion = entry_identificacion
        self.entry_conta = entry_conta
        # Usamos None para verificar si un objeto o variable tiene un valor de None
        self.cliente1 = None

        #Usaremos Button para crear botones en una interfaz gráfica.
        #Usaremos text  para establecer el texto en el botón 
        #Usamos command para especificar la función que debe ejecutarse cuando el usuario interactúa con el widget al que se le asigna este parámetro
        depositar = Button(orin, text="Depositar", command=self.deposito)
        #Usaremos pack  para organizar y colocar un widget dentro de su contenedor principal
        depositar.pack()
        
        #Usaremos Button para crear botones en una interfaz gráfica.
        #Usaremos text  para establecer el texto en el botón 
        #Usamos command para especificar la función que debe ejecutarse cuando el usuario interactúa con el widget al que se le asigna este parámetro
        retirar = Button(orin, text="Retirar", command=self.retiro)
        #Usaremos pack  para organizar y colocar un widget dentro de su contenedor principal
        retirar.pack()

        #Usaremos Button para crear botones en una interfaz gráfica. 
        #Usaremos text  para establecer el texto en el botón 
        #Usamos command para especificar la función que debe ejecutarse cuando el usuario interactúa con el widget al que se le asigna este parámetro
        salida = Button(orin, text="Salir", command=self.salir)
        #Usaremos pack  para organizar y colocar un widget dentro de su contenedor principal
        salida.pack()
    #Usamos el def para definir una funcion de codigo reutilizable
    def deposito(self):
        #Usaremos if not para verificar si una condición es falsa
        if not self.campos_llenos():
            #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas
            #Usamos showwarning para mostrar un cuadro de diálogo de advertencia.
            messagebox.showwarning("Campos incompletos", "Por favor completa todas las cajas de texto antes de realizar un depósito")
            #Usaremos return para devolver un valor específico al punto de llamada de la función
            return
        #Usaremos try para manejar excepciones o errores que pueden ocurrir durante la ejecución de un programa
        try:
            depositar = simpledialog.askinteger("Depositar", "Ingresa la cantidad a depositar")
            #Usamos el if para controlar el flujo de una condicion 
            # Usamos None para verificar si un objeto o variable tiene un valor de None
            #Usamos is para verifica la identidad del objeto, mientras que == verifica la igualdad de valor.
            if self.cliente1 is None:
                self.crear_cliente()
                
            #Usaremos simpledialog para crear cuadros de diálogo en aplicaciones gráficas.
            #Usaremos askinteger para mostrar un cuadro de diálogo que solicita al usuario ingresar un número entero.
            #Usamos el if para controlar el flujo de una condicion 
            if depositar:
                resul = self.cliente1.tipo("deposito", depositar, 0, 0)
                #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas.
                #Usaremos showinfo para mostrar un cuadro de diálogo de información.
                messagebox.showinfo("Su depósito ha sido realizado con éxito!. Y tienes en tu cuenta un total de", resul)
                self.mostrar_saldo()
        #Usamos el except para  tratar posibles errores que ocurren durante la ejecución de un programa
        except ValueError:
            #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas
            #Usamos showerror Esta función se utiliza para mostrar un cuadro de diálogo que informa sobre un error.
            messagebox.showerror("Error por favor querido usuario nada mas ingresa valores numericos")

    #Usamos el def para definir una funcion de codigo reutilizable
    def campos_llenos(self):
        #Usaremos if not para verificar si una condición es falsa
        #or es un operador lógico que devuelve True si al menos una de las condiciones es verdadera. not es un operador de negación que invierte el valor de la condición.
        if not entry_nombre.get() or not entry_identificacion.get() or not entry_conta.get(): 
            #Usamos return False para indicar que la función debe devolver el valor booleano False
            return False
        #Usaremos return true para indicar que la función debe devolver el valor booleano True
        return True
    #Usamos el def para definir una funcion de codigo reutilizable
    def retiro(self):
        #Usaremos if not para verificar si una condición es falsa
        if not self.campos_llenos():
            #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas
            #Usamos showwarning para mostrar un cuadro de diálogo de advertencia.
            messagebox.showwarning("Campos incompletos", "Por favor completa todas las cajas de texto antes de realizar un retiro")
            #Usaremos return para devolver un valor específico al punto de llamada de la función
            return 
        #Usamos el if para controlar el flujo de una condicion 
        if self.cliente1 is None:
            self.crear_cliente()
        #Usaremos try para manejar excepciones o errores que pueden ocurrir durante la ejecución de un programa
        try:
            retirar = simpledialog.askinteger("Retirar", "Ingresa la cantidad a retirar:")
            #Usaremos simpledialog para crear cuadros de diálogo en aplicaciones gráficas.
            #Usaremos askinteger para mostrar un cuadro de diálogo que solicita al usuario ingresar un número entero.
            #Usamos el if para controlar el flujo de una condicion 
            if retirar:
                    resultado = self.cliente1.tipo("retiro", retirar, self.cliente1.numero_identificacion, self.cliente1.contraseña)
                    #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas.
                    #Usaremos showinfo para mostrar un cuadro de diálogo de información.
                    messagebox.showinfo("Resultado", resultado)
                    self.mostrar_saldo()
        #Usamos el except para  tratar posibles errores que ocurren durante la ejecución de un programa
        except ValueError:
            #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas
            #Usamos showerror Esta función se utiliza para mostrar un cuadro de diálogo que informa sobre un error.
            messagebox.showerror("Error por favor querido usuario nada más ingresa valores numéricos")
    #Usamos el def para definir una funcion de codigo reutilizable
    def salir(self):
        self.orin.quit()
    #Usamos el def para definir una funcion de codigo reutilizable
    def mostrar_saldo(self):
        #Usamos el if para controlar el flujo de una condicion 
        if self.cliente1:
            saldo_actual = self.cliente1.saldos
            #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas.
            #Usaremos showinfo para mostrar un cuadro de diálogo de información.
            messagebox.showinfo("Saldo actual", f"Tu saldo actual es de {saldo_actual} pesos.")
    #Usamos el def para definir una funcion de codigo reutilizable
    def crear_cliente(self):
        #Usaremos simpledialog para crear cuadros de diálogo en aplicaciones gráficas.
        #Usaremos askinteger para mostrar un cuadro de diálogo que solicita al usuario ingresar un número entero.
        entry_nombre = simpledialog.askstring("Crear cliente", "Ingresa tu nombre:", parent=aplicacion)
        #Usaremos simpledialog para crear cuadros de diálogo en aplicaciones gráficas.
        #Usaremos askinteger para mostrar un cuadro de diálogo que solicita al usuario ingresar un número entero.
        entry_identificacion = simpledialog.askinteger("Crear cliente", "Ingresa tu numero de identificación:", parent=aplicacion)
        #Usaremos simpledialog para crear cuadros de diálogo en aplicaciones gráficas.
        #Usaremos askinteger para mostrar un cuadro de diálogo que solicita al usuario ingresar un número entero.
        entry_conta = simpledialog.askinteger("Crear cliente", "Ingresa tu contraseña:", parent=aplicacion)
        #Usamos el if para controlar el flujo de una condicion 
        if (
            entry_nombre == self.entry_nombre.get()
            #Usamos and es una palabra clave utilizada como un operador lógico para combinar condiciones en expresiones booleanas.
            and entry_identificacion == int(self.entry_identificacion.get())
            #Usamos and es una palabra clave utilizada como un operador lógico para combinar condiciones en expresiones booleanas.
            and entry_conta == int(self.entry_conta.get())):

            self.cliente1 = Cliente(entry_nombre, entry_identificacion, entry_conta)
            #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas.
            #Usaremos showinfo para mostrar un cuadro de diálogo de información.
            messagebox.showinfo("Éxito", "Los datos coinciden con los valores guardados.")
        #Usamos else para  cuando la condición del "if" es evaluada como falsa
        else:
            #Usaremos messagebox para mostrar cuadros de diálogo de mensajes en aplicaciones gráficas
            #Usamos showerror Esta función se utiliza para mostrar un cuadro de diálogo que informa sobre un error.
            messagebox.showerror(
                "Error",
                "Los datos ingresados no coinciden con los valores guardados.")
            

#Usaremos Button para crear botones en una interfaz gráfica.
#Usaremos text  para establecer el texto en el botón 
#Usamos command para especificar la función que debe ejecutarse cuando el usuario interactúa con el widget al que se le asigna este parámetro
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
boton2 = Button(aplicacion, text="Depósito", fg="purple", command=tex(aplicacion).deposito)
boton2.place(relx=0.1, rely=0.6, anchor="w")

#Usaremos Button para crear botones en una interfaz gráfica.
#Usaremos text  para establecer el texto en el botón 
#Usamos command para especificar la función que debe ejecutarse cuando el usuario interactúa con el widget al que se le asigna este parámetro
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
boton3 = Button(aplicacion, text="Retiro", fg="purple", command=tex(aplicacion).retiro)
boton3.place(relx=0.4, rely=0.6, anchor="w")

#Usamoa Label  para mostrar texto o imágenes en una interfaz
#Usaremos text  para establecer el texto en el botón 
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
boton4 = Label(aplicacion, text="Si deseas salir del programa da click en el botón de salir", fg="purple", font=("Bell MT", 10))
boton4.place(relx=0.1, rely=0.7, anchor="w")
#Usaremos Button para crear botones en una interfaz gráfica.
#Usaremos text  para establecer el texto en el botón 
#Usamos command para especificar la función que debe ejecutarse cuando el usuario interactúa con el widget al que se le asigna este parámetro
#Usamos place para colocar un widget en una ubicación específica dentro de su contenedor.
boton5 = Button(aplicacion, text="Salir", fg="purple", command=tex(aplicacion).salir)
boton5.place(relx=0.4, rely=0.7, anchor="w")
print("Chau saliste del programa")


#Usaremos mainloop() para iniciar el bucle principal del programa.  
aplicacion.mainloop()