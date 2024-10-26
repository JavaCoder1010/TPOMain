# Trabajo Práctico Obligatorio

TPO es el proyecto final de la materia de "Introducción a la Algoritmia" de UADE, a cargo del profesor Guillermo Maqueira. Consiste en un programa que permite a un contribuyente declarar sus fondos. El programa permite al usuario ingresar sus datos personales, edad, fecha de nacimiento y profesin, adems de los fondos que va a declarar.

## Requisitos

- Python 3.7 o superior
- Tkinter (ya viene incluido con Python)

## Uso

1. Clonar el repositorio: `git clone https://github.com/JavaCoder1010/TPOMain.git`
2. Entrar en la carpeta del proyecto: `cd TPOMain`
3. Iniciar el programa: `python main.py`
4. Ingresar los datos personales y los fondos a declarar
5. Pulsar el botn "Enviar"
6. Ver la lista de todos los contribuyentes que han declarado fondos: pulsar el botn "Mostrar datos"

## Estructura del archivo

project/
│
├── frontend/
│   ├── interfaz.py                 # Contendrá la lógica para inicializar la ventana principal
│   ├── campos.py                   # Funciones para crear los campos de entrada
│   ├── checkboxes.py              # Funciones para crear los checkboxes
│   ├── botones.py                 # Funciones para crear los botones
│
├── listas.py                      # Contiene las listas globales
├── manejo_errores.py             # Archivo de manejo de errores
├── limpiar.py                    # Funciones para limpiar el formulario
├── ver_datos.py                  # Funciones para visualizar los datos
└── main.py                       # Archivo principal

## Alumnos

- Menta Patricio
- Gastón Martinez
- Veis Andrei
