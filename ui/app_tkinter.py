import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from sistema.gestor_sistema import GestorSistema
from clases.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from test.simulaciones import ejecutar_simulaciones
from utilidades.logger import registrar_error, registrar_evento


class AppTkinter:
    def __init__(self, gestor: GestorSistema) -> None:
        self.gestor: GestorSistema = gestor

        self.ventana: tk.Tk = tk.Tk()
        self.ventana.title("Sistema de Reservas - Software FJ")
        self.ventana.geometry("950x650")
        self.ventana.minsize(850, 550)

        self.style: ttk.Style = ttk.Style()
        self.aplicar_tema()

        self.crear_interfaz()

    def aplicar_tema(self) -> None:
        self.style.theme_use("clam")

        self.style.configure(
            "TFrame",
            background="#a6cce9"
        )

        self.style.configure(
            "TLabel",
            background="#a6cce9",
            font=("Segoe UI", 10)
        )

        self.style.configure(
            "Title.TLabel",
            background="#a6cce9",
            font=("Segoe UI", 18, "bold")
        )

        self.style.configure(
            "TButton",
            background = "#588cb3",
            foreground= "#000000",

            font=("Segoe UI", 10),
            padding=6
        )

        self.style.configure(
            "TEntry",
            padding=4
        )

        self.style.configure(
            "TLabelframe",
            background="#a6cce9"
        )

        self.style.configure(
            "TLabelframe.Label",
            background="#a6cce9",
            font=("Segoe UI", 12, "bold")
        )

    def crear_interfaz(self) -> None:
        self.contenedor: ttk.Frame = ttk.Frame(self.ventana, padding=16)
        self.contenedor.grid(row=0, column=0, sticky="nsew")

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.contenedor.columnconfigure(0, weight=1)
        self.contenedor.columnconfigure(1, weight=2)
        self.contenedor.rowconfigure(2, weight=1)

        self.titulo: ttk.Label = ttk.Label(
            self.contenedor,
            text="Sistema Integral de Gestión de Clientes, Servicios y Reservas",
            style="Title.TLabel"
        )
        self.titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(0, 16)
        )

        self.crear_panel_cliente()
        self.crear_panel_acciones()
        self.crear_panel_resultados()

    def crear_panel_cliente(self) -> None:
        self.frame_cliente: ttk.LabelFrame = ttk.LabelFrame(
            self.contenedor,
            text="Registro de cliente",
            padding=12
        )
        self.frame_cliente.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        self.frame_cliente.columnconfigure(0, weight=0)
        self.frame_cliente.columnconfigure(1, weight=1)

        self.label_identificacion: ttk.Label = ttk.Label(
            self.frame_cliente,
            text="Identificación:"
        )
        self.label_identificacion.grid(
            row=0,
            column=0,
            sticky="w",
            pady=5
        )

        self.entrada_identificacion: ttk.Entry = ttk.Entry(self.frame_cliente)
        self.entrada_identificacion.grid(
            row=0,
            column=1,
            sticky="ew",
            pady=5
        )

        self.label_nombre: ttk.Label = ttk.Label(
            self.frame_cliente,
            text="Nombre:"
        )
        self.label_nombre.grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.entrada_nombre: ttk.Entry = ttk.Entry(self.frame_cliente)
        self.entrada_nombre.grid(
            row=1,
            column=1,
            sticky="ew",
            pady=5
        )

        self.label_correo: ttk.Label = ttk.Label(
            self.frame_cliente,
            text="Correo:"
        )
        self.label_correo.grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        self.entrada_correo: ttk.Entry = ttk.Entry(self.frame_cliente)
        self.entrada_correo.grid(
            row=2,
            column=1,
            sticky="ew",
            pady=5
        )

        self.boton_registrar_cliente: ttk.Button = ttk.Button(
            self.frame_cliente,
            text="Registrar cliente",
            command=self.registrar_cliente_desde_ui
        )
        self.boton_registrar_cliente.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(12, 5)
        )

    def crear_panel_acciones(self) -> None:
        self.frame_acciones: ttk.LabelFrame = ttk.LabelFrame(
            self.contenedor,
            text="Acciones del sistema",
            padding=12
        )
        self.frame_acciones.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        self.frame_acciones.columnconfigure(0, weight=1)
        self.frame_acciones.columnconfigure(1, weight=1)

        self.boton_crear_servicios: ttk.Button = ttk.Button(
            self.frame_acciones,
            text="Crear servicios de prueba",
            command=self.crear_servicios_prueba
        )
        self.boton_crear_servicios.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )

        self.boton_simulaciones: ttk.Button = ttk.Button(
            self.frame_acciones,
            text="Ejecutar simulaciones",
            command=self.ejecutar_simulaciones_desde_ui
        )
        self.boton_simulaciones.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        self.boton_ver_log: ttk.Button = ttk.Button(
            self.frame_acciones,
            text="Ver log",
            command=self.mostrar_log
        )
        self.boton_ver_log.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        self.boton_listar_clientes: ttk.Button = ttk.Button(
            self.frame_acciones,
            text="Listar clientes",
            command=self.listar_clientes_desde_ui
        )
        self.boton_listar_clientes.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )

        self.boton_listar_servicios: ttk.Button = ttk.Button(
            self.frame_acciones,
            text="Listar servicios",
            command=self.listar_servicios_desde_ui
        )
        self.boton_listar_servicios.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )

        self.boton_limpiar: ttk.Button = ttk.Button(
            self.frame_acciones,
            text="Limpiar pantalla",
            command=self.limpiar_resultados
        )
        self.boton_limpiar.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

    def crear_panel_resultados(self) -> None:
        self.frame_resultados: ttk.LabelFrame = ttk.LabelFrame(
            self.contenedor,
            text="Resultados de la sesión",
            padding=12
        )
        self.frame_resultados.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=(12, 0)
        )

        self.frame_resultados.columnconfigure(0, weight=1)
        self.frame_resultados.rowconfigure(0, weight=1)

        self.resultado_texto: tk.Text = tk.Text(
            self.frame_resultados,
            height=18,
            wrap="word",
            font=("Consolas", 10)
        )
        self.resultado_texto.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.scroll_resultado: ttk.Scrollbar = ttk.Scrollbar(
            self.frame_resultados,
            orient="vertical",
            command=self.resultado_texto.yview
        )
        self.scroll_resultado.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.resultado_texto.configure(
            yscrollcommand=self.scroll_resultado.set
        )

    def escribir_resultado(self, mensaje: str) -> None:
        self.resultado_texto.insert(tk.END, mensaje + "\n")
        self.resultado_texto.see(tk.END)

    def limpiar_resultados(self) -> None:
        self.resultado_texto.delete("1.0", tk.END)

    def registrar_cliente_desde_ui(self) -> None:
        try:
            identificacion: str = self.entrada_identificacion.get()
            nombre: str = self.entrada_nombre.get()
            correo: str = self.entrada_correo.get()

            cliente = self.gestor.registrar_cliente(
                identificacion,
                nombre,
                correo
            )

            self.escribir_resultado("=== CLIENTE REGISTRADO ===")
            self.escribir_resultado(cliente.mostrar_informacion())

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado correctamente."
            )

        except Exception as error:
            registrar_error(f"Error al registrar cliente desde interfaz: {error}")
            self.escribir_resultado(f"ERROR: {error}")
            messagebox.showerror("Error", str(error))

    def crear_servicios_prueba(self) -> None:
        try:
            servicio_1: ReservaSala = ReservaSala("Sala principal", 50000)
            servicio_2: AlquilerEquipo = AlquilerEquipo("Video Beam", 25000)
            servicio_3: AsesoriaEspecializada = AsesoriaEspecializada(
                "Asesoría técnica",
                80000
            )

            self.gestor.registrar_servicio(servicio_1)
            self.gestor.registrar_servicio(servicio_2)
            self.gestor.registrar_servicio(servicio_3)

            self.escribir_resultado("=== SERVICIOS CREADOS ===")
            self.escribir_resultado(servicio_1.describir())
            self.escribir_resultado(servicio_2.describir())
            self.escribir_resultado(servicio_3.describir())

            messagebox.showinfo(
                "Éxito",
                "Servicios de prueba creados correctamente."
            )

        except Exception as error:
            registrar_error(f"Error al crear servicios desde interfaz: {error}")
            self.escribir_resultado(f"ERROR: {error}")
            messagebox.showerror("Error", str(error))

    def ejecutar_simulaciones_desde_ui(self) -> None:
        try:
            resultados: list[str] = ejecutar_simulaciones()

            self.escribir_resultado("")
            self.escribir_resultado("=== SIMULACIONES DEL SISTEMA ===")

            for mensaje in resultados:
                self.escribir_resultado(mensaje)

            self.escribir_resultado("=== FIN DE SIMULACIONES ===")
            self.escribir_resultado("")

            registrar_evento("Simulaciones ejecutadas desde la interfaz.")

            messagebox.showinfo(
                "Simulaciones",
                "Las simulaciones se ejecutaron correctamente."
            )

        except Exception as error:
            registrar_error(f"Error general al ejecutar simulaciones: {error}")
            self.escribir_resultado(f"ERROR GENERAL EN SIMULACIONES: {error}")
            messagebox.showerror("Error", str(error))

    def listar_clientes_desde_ui(self) -> None:
        try:
            clientes = self.gestor.listar_clientes()

            self.escribir_resultado("")
            self.escribir_resultado("=== CLIENTES REGISTRADOS ===")

            if len(clientes) == 0:
                self.escribir_resultado("No hay clientes registrados.")
                return

            for cliente in clientes:
                self.escribir_resultado(cliente.mostrar_informacion())

        except Exception as error:
            registrar_error(f"Error al listar clientes: {error}")
            self.escribir_resultado(f"ERROR: {error}")
            messagebox.showerror("Error", str(error))

    def listar_servicios_desde_ui(self) -> None:
        try:
            servicios = self.gestor.listar_servicios()

            self.escribir_resultado("")
            self.escribir_resultado("=== SERVICIOS REGISTRADOS ===")

            if len(servicios) == 0:
                self.escribir_resultado("No hay servicios registrados.")
                return

            for servicio in servicios:
                self.escribir_resultado(servicio.describir())

        except Exception as error:
            registrar_error(f"Error al listar servicios: {error}")
            self.escribir_resultado(f"ERROR: {error}")
            messagebox.showerror("Error", str(error))

    def mostrar_log(self) -> None:
        try:
            ruta_log: Path = Path("logs/eventos.log")

            self.escribir_resultado("")
            self.escribir_resultado("=== CONTENIDO DEL LOG ===")

            if not ruta_log.exists():
                self.escribir_resultado("Todavía no existe archivo de log.")
                return

            contenido: str = ruta_log.read_text(encoding="utf-8")

            if contenido.strip() == "":
                self.escribir_resultado("El archivo de log está vacío.")
                return

            self.escribir_resultado(contenido)

        except Exception as error:
            self.escribir_resultado(f"ERROR AL LEER LOG: {error}")
            messagebox.showerror("Error", str(error))

    def ejecutar(self) -> None:
        self.ventana.mainloop()