from sistema.gestor_sistema import GestorSitema
from ui.app_tkinter import AppTkinter

def main() -> None:
    gestor: GestorSitema = GestorSitema()
    app: AppTkinter = AppTkinter(gestor)
    app.ejecutar()

if __name__ == "__main__":
    main()
