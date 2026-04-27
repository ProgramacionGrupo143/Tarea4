# Guía de trabajo colaborativo
Este documento define la forma de trabajo del equipo para el proyecto Fase 4 del curso Programación. Su objetivo es evitar errores de integración, mantener una estructura ordenada y facilitar el trabajo colaborativo en GitHub.

## 1. Forma correcta de abrir el proyecto

El proyecto debe abrirse como carpeta completa desde Visual Studio Code:

fase4-unad-programacion/

**No abrir archivos sueltos como:**
cliente.py
servicio.py
reserva.py

## 2. Forma correcta de ejecutar el proyecto

El proyecto se ejecuta desde la carpeta raíz:

python main.py

**No ejecutar archivos internos directamente:**

python clases/cliente.py
python clases/reserva.py
python utilidades/logger.py


## 3. Flujo del sistema

main.py 

-> SE RELACIONA CON

interfaz/app_tkinter.py

-> SE RELACIONA CON

logica/gestor_sistema.py

-> SE RELACIONA CON

clases/cliente.py
clases/servicio.py
clases/reserva.py

-> SE RELACIONA CON

utilidades/errores.py
utilidades/logger.py


## 4. Flujo del sistema

**Compañero 1 — cliente.py**

Debe implementar la clase Cliente.

Debe cumplir:
Validar identificación.
Validar nombre.
Validar correo.
Aplicar encapsulación.
Lanzar DatosInvalidosError cuando corresponda.
Crear método mostrar_informacion().

No debe modificar:
main.py
app_tkinter.py
gestor_sistema.py

**Compañero 2 — servicio.py**

Debe implementar:
Clase abstracta Servicio.
Clase ReservaSala.
Clase AlquilerEquipo.
Clase AsesoriaEspecializada.

Debe cumplir:
Validar nombre del servicio.
Validar precio mayor que cero.
Implementar calcular_costo().
Implementar describir().
Aplicar herencia y polimorfismo.


## 5. Estandar de Codigo

- Nombres de archivos : Usar minúsculas
- Nombres de clases: Usar PascalCase  
- Variables y funciones: Usar snake_case 