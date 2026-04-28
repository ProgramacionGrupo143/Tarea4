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


## 4. Responsabilidades de equipo

**Lider de proyecto — Miguel Alvarez**

- Archivo Asignado : main.py, interfaz/app_tkinter.py, logica/gestor_sistema.py, utilidades/logger.py, pruebas/simulaciones.py, README.md, CONTRIBUTING.md

- Responsabilidad: Debe integrar todo el sistema, unir los módulos de los compañeros, crear la interfaz gráfica, manejar logs, realizar pruebas y preparar la entrega final.

- Datos que debe recibir : Cliente, Servicio, Reserva y errores personalizados.

- Validaciones : el proyecto debe ejecutar desde main.py, imports funcionando, interfaz estable, logs funcionando, simulaciones correctas.

- TIPS: main.py inicia todo el sistema. gestor_sistema.py coordina listas internas. app_tkinter.py captura datos y llama funciones. logger.py guarda eventos y errores. simulaciones.py prueba casos validos e invalidos.

Debe cumplir:
Crear estructura del proyecto.
Revisar imports.
Integrar módulos.
Crear interfaz Tkinter.
Implementar logs.
Implementar simulaciones.
Verificar ejecución con python main.py.
Preparar README.
Preparar PDF final.

No debe modificar:
Nada sin revisar integración general.

**Compañero 1 - NN**

- Archivo Asignado : clases/clientes.py

- Responsabilidad: Debe crear la clase Cliente. que representa a una persona que puede hacer uan reserva dentro del sistema.

- Datos que debe recibir : indetificacion(str), nombre(str),correo(str) 

- Validaciones : indentificacion no esta vacia, nombre no esta vacio, correo no esta vacio, correo tenga simbolo @

- TIPS: @properity -> ermite consultar dato privado como si fuese varible normal. Si un dato esta mal debe lanzar error usando  rasise ejemplo: raise DatosInvalidosERROR("El nombre no puede estar vacio").

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

**Compañero 2 — Nicolas Ariza**

- Archivo Asignado : clases/reserva.py

- Responsabilidad: Debe crear la clase Reserva. que representa la union entre un cliente, un servicio y una duración dentro del sistema.

- Datos que debe recibir : cliente(Cliente), servicio(Servicio), duracion_horas(int)

- Validaciones : duracion_horas mayor que cero, servicio disponible, no confirmar reserva cancelada, no cancelar reserva confirmada

- TIPS: Este archivo recibe objetos ya creados de Cliente y Servicio. raise sirve para lanzar error ejemplo: raise ReservaInvalidaError("La duración debe ser mayor que cero").

Debe cumplir:
Recibir cliente.
Recibir servicio.
Recibir duración.
Validar duración mayor que cero.
Validar servicio disponible.
Calcular costo total.
Manejar estado pendiente.
Manejar estado confirmada.
Manejar estado cancelada.
Crear método confirmar().
Crear método cancelar().
Crear método mostrar_informacion().

No debe modificar:
main.py
app_tkinter.py
gestor_sistema.py
cliente.py
servicio.py
logger.py
simulaciones.py

**Compañero 2 — Dyana Gonzalez**

- Archivo Asignado : clases/servicio.py

- Responsabilidad: Debe crear la clase abstracta Servicio y las clases hijas ReservaSala, AlquilerEquipo y AsesoriaEspecializada. Representa los servicios que ofrece la empresa.

- Datos que debe recibir : nombre(str), precio_base(float)

- Validaciones : nombre no esta vacio, precio_base mayor que cero

- TIPS: ABC -> sirve para crear clase abstracta. @abstractmethod -> obliga a las clases hijas a crear sus propios metodos. raise sirve para lanzar error ejemplo: raise DatosInvalidosError("El precio base debe ser mayor que cero").

Debe cumplir:
Crear clase Servicio.
Crear clase ReservaSala.
Crear clase AlquilerEquipo.
Crear clase AsesoriaEspecializada.
Validar nombre del servicio.
Validar precio mayor que cero.
Implementar calcular_costo().
Implementar describir().
Aplicar herencia.
Aplicar polimorfismo.

No debe modificar:
main.py
app_tkinter.py
gestor_sistema.py
cliente.py
logger.py
simulaciones.py

## 5. Estandar de Codigo

- Nombres de archivos : Usar minúsculas
- Nombres de clases: Usar PascalCase  
- Variables y funciones: Usar snake_case 