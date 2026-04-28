import tkinter as tk
from tkinter import messagebox

from sistema.gestor_sistema import GestorSitema
from utilidades.logger import registrar_error

class AppTkinter:
    def __init__(self,gestor:GestorSitema)-> None:
        self.gestor : GestorSitema = gestor
        self.ventana : tk.Tk = tk.Tk()

        self.ventana.title("Sistema de Reservas - Software")
        self.ventana.geometry("700x550")

    def registar_clientes(self)-> None:
        try:
            pass
        except Exception as error:
            registrar_error(str(error))
            messagebox.showerror("Error",str(error))

    def crear_servicio(self)-> None:
        try:
            pass
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