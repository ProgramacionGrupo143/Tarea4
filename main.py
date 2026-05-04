from sistema.gestor_sistema import GestorSistema
from ui.app_tkinter import AppTkinter

def main() -> None:
    gestor: GestorSistema = GestorSistema()
    app: AppTkinter = AppTkinter(gestor)
    app.ejecutar()

if __name__ == "__main__":
    main()
