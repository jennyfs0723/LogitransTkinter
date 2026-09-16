# importamos los modulos de tkinter
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("LOGITRANS - Sistema de Distribución")
root.geometry("650x450")

# Configuracion del sistema, con esto en la parte de arriba sabremos quien es el que esta accediendo al "Portal"
class ConfigSistema:
    VERSION = "v1"
    FECHA = "20/08/2026"
    CLIENTE = "Jenny Florez"
    EMPRESA = "Logitrans"

# Creamos un metodo para que los datos aparezcan en el encabezado
    @classmethod
    def obtener_encabezado(cls):
        return f"Cliente: {cls.CLIENTE}  |  Versión: {cls.VERSION}  |  Fecha: {cls.FECHA}  |  Empresa: {cls.EMPRESA}"


# visual del modulo 1
lbl_meta = tk.Label(root, text=ConfigSistema.obtener_encabezado(), font=("Arial", 9, "bold"),
        bg="#2C3E50", fg="white", pady=5)
lbl_meta.pack(side=tk.TOP, fill=tk.X)  # para pegar el encabezado en la parte superior y ordenamos que se expanda
# Gestion de clientes y pedidos
class ModuloCliente:
    @staticmethod
    def registrar_cliente_accion():
        messagebox.showinfo(
            "Logitrans - Clientes","El Cliente se ha registrado con exito!."
        )

# Creamos la ventana principal
    @classmethod
    def crear_pestana(cls,principal):
        frame = tk.LabelFrame(principal, text=" Datos de Creacion de cliente ", padx=15, pady=15)  # --> Tamaño
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        tk.Label(frame, text="Nombre completo/Empresa:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=20).grid(row=1, column=1, sticky="w", pady=5, padx=5)
        tk.Label(frame, text="Cc / Nit:").grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=30).grid(row=2, column=1, sticky="w", pady=5, padx=5)
        tk.Label(frame, text="Correo electronico").grid(row=3, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=30).grid(row=3, column=1, sticky="w", pady=5, padx=5)

# Creacion del boton
        btn_guardar = tk.Button(
            frame,
            text="Registrar Cliente",
            command=cls.registrar_cliente_accion,
            bg="#27AE60",
            fg="white",
            font=("Arial", 10, "bold")
        )
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=20)

#Gestion de envios y clientes
class ModuloEnvios:
    @staticmethod
    def registrar_envio_accion():
        messagebox.showinfo(
            "Logitrans - Envíos",
            "¡Operación Exitosa!\nLa orden de envío ha sido validada por el sistema.")

# Creacion de la ventana principal
    @classmethod
    def crear_pestana(cls, principal):
        frame = tk.LabelFrame(principal, text=" Datos de la Guía de Distribución ", padx=15, pady=15) # --> Tamaño
        frame.pack(pady=20, padx=20, fill="both", expand=True) # La podemos agrandar lo que queramos
# Fill = both es para estirar en todas las direcciones al mismo tiempo

        tk.Label(frame, text="Número de Guía:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=20).grid(row=0, column=1, sticky="w", pady=5, padx=5)
# Por medio de grid creamos los elementos en forma de tabla. row es renglon y column es columna
# y por medio de sticky = w estamos pegando el texto hacia la izquierda
# uno es un frame y el otro es la entrada para ungresar texto
        tk.Label(frame, text="Cliente / RUC:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=30).grid(row=1, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame, text="Dirección Destino:").grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=40).grid(row=2, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame, text="Peso Declarado (Kg):").grid(row=3, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=15).grid(row=3, column=1, sticky="w", pady=5, padx=5)

# Creacion del boton.
        btn_guardar = tk.Button(
            frame, 
            text="Generar Guía de Envío", 
            command=cls.registrar_envio_accion, 
            bg="#27AE60", 
            fg="white", 
            font=("Arial", 10, "bold")
        )
        btn_guardar.grid(row=4, column=0, columnspan=2, pady=20)


# control de flota y envios
class ModuloFlota:
    @staticmethod
    def asignar_transporte_accion():
        # Enviamos ventana de emergencia
        messagebox.showwarning(
            "LogiTrans - Flota", 
            "Validación de Recursos:\nEl vehículo seleccionado y el conductor se encuentran disponibles en ruta."
        )

    @classmethod
    def crear_pestana(cls, principal):
        frame = tk.LabelFrame(principal, text=" Asignación de Recursos de Transporte ", padx=15, pady=15)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        tk.Label(frame, text="Placa del Vehículo:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=20).grid(row=0, column=1, sticky="w", pady=5, padx=5)
 # width = .. es el ancho visual del componente en pantalla
        tk.Label(frame, text="Código del Conductor:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=20).grid(row=1, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame, text="Ruta de Distribución:").grid(row=2, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=35).grid(row=2, column=1, sticky="w", pady=5, padx=5)
# Creacion de boton
        btn_asignar = tk.Button(
            frame, 
            text="Vincular Conductor y Camión", 
            command=cls.asignar_transporte_accion, 
            bg="#2980B9", 
            fg="white", 
            font=("Arial", 10, "bold")
        )
        btn_asignar.grid(row=3, column=0, columnspan=2, pady=25) # columnspan es para expandir el boton
        # las columnas necesarias


#Reporte de incidentes y riesgos
class ModuloIncidentes:
    @staticmethod
    def lanzar_alerta_accion():
        # Mensaje de error
        messagebox.showerror(
            "LOGITRANS - ALERTA CRÍTICA", 
            "¡Incidente Reportado!\nSe ha notificado al Centro de Distribución y las "
            "coordenadas GPS han sido enviadas."
        )

    @classmethod
    def crear_pestana(cls, principal):
        frame = tk.LabelFrame(principal, text=" Reporte de Novedades e Incidentes en Ruta ", padx=15, pady=15)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        tk.Label(frame, text="Ubicación Actual (GPS):").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=30).grid(row=0, column=1, sticky="w", pady=5, padx=5)

        tk.Label(frame, text="Descripción del Incidente:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame, width=45).grid(row=1, column=1, sticky="w", pady=5, padx=5)
# Creacion de boton
        btn_alerta = tk.Button(
            frame, 
            text="Emitir Alerta Logística", 
            command=cls.lanzar_alerta_accion, 
            bg="#C0392B", 
            fg="white", 
            font=("Arial", 10, "bold")
        )
        btn_alerta.grid(row=2, column=0, columnspan=2, pady=25)


# Contenedor de pestañas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# Crear contenedores de cada pestaña
pestana1 = ttk.Frame(notebook)
pestana2 = ttk.Frame(notebook)
pestana3 = ttk.Frame(notebook)
pestana4 = ttk.Frame(notebook)

# Agrergamos las pestañas a los contenedores vacios
notebook.add(pestana1, text = "Registro de clientes")
notebook.add(pestana2, text="Registro de Envíos")
notebook.add(pestana3, text="Control de Flota")
notebook.add(pestana4, text="Reporte de Incidentes")


# Inicialización visual de los Módulos 2, 3 y 4
ModuloCliente.crear_pestana(pestana1)
ModuloEnvios.crear_pestana(pestana2)
ModuloFlota.crear_pestana(pestana3)
ModuloIncidentes.crear_pestana(pestana4)

root.mainloop()