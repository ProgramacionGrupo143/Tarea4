import tkinter as tk
from tkinter import messagebox

from sistema.gestor_sistema import GestorSitema
from clases.servicio import ReservarSala, AlquilerEquipo, AsesoriaEspecializada
from utilidades.logger import registrar_error

class AppTkinter:
    def __init__(self,gestor:GestorSitema)-> None:
        self.gestor : GestorSitema = gestor
        self.ventana : tk.Tk = tk.Tk()

        self.ventana.title("Sistema de Reservas - Software")
        self.ventana.geometry("700x550")


        self.label_identificacion : tk.Label = tk.Label(text="Identificacion :")
        self.label_nombre : tk.Label = tk.Label(text="Nombre: ")
        self.Label_correo : tk.Label = tk.Label(text="Correo :")

        self.entrada_identificaion : tk.Entry = tk.Entry(self.ventana)
        self.entrada_nombre : tk.Entry = tk.Entry(self.ventana)
        self.entrada_correo : tk.Entry = tk.Entry(self.ventana)

        self.label_identificacion.pack()
        self.entrada_identificaion.pack()
        self.label_nombre.pack()
        self.entrada_nombre.pack()
        self.Label_correo.pack()
        self.entrada_correo.pack()

        self.boton_registrar : tk.Button = tk.Button(
             self.ventana,
             text="Registrar Cliente",
             command=self.registar_clientes
        )
        self.boton_registrar.pack()

        self.boton_servicios : tk.Button = tk.Button(
             self.ventana,
             text="Crear Servicios de Prueba",
             command=self.crear_servicio_prueba
        )
        self.boton_servicios.pack()

        self.resultado : tk.Text = tk.Text(self.ventana,height=10)
        self.resultado.pack()

    def registar_clientes(self)-> None:
        try:
            identificacion : str = self.entrada_identificaion.get()
            nombre : str = self.entrada_nombre.get()
            correo : str = self.entrada_correo.get()

            cliente = self.gestor.registar_cliente(identificacion,nombre,correo)

            messagebox.showinfo("Exito","Cliente registrado correctamente")
            self.resultado.insert(tk.END,cliente.mostrar_informacion()+ "\n")

        except Exception as error:
            registrar_error(str(error))
            messagebox.showerror("Error",str(error))

    def crear_servicio_prueba(self)-> None:
        try:
            self.gestor.registar_servicio(ReservarSala("Sala principal",500000))
            self.gestor.registar_servicio(AlquilerEquipo("Portatil Mac"),"30000")
            self.gestor.registar_servicio(AsesoriaEspecializada("Asesoria Tencnica",80000))

            messagebox.showinfo("Exito","Servicio creado correctamente")

        except Exception as error:
                registrar_error(str(error))
                messagebox.showerror("Error",str(error))

    def crear_reserva(self)-> None:
        try:
            pass
        except Exception as error:
                registrar_error(str(error))
                messagebox.showerror("Error",str(error))

    def ejecutar(self)-> None:
        self.ventana.mainloop()