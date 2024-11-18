import tkinter as tk
from ver_datos import mostrar_datos
from listas import (
    dniLista,
    apellidoLista,
    nombreLista,
    edadLista,
    fechaDeNacimientoLista,
    profesionLista,
    montoLista,
    fechaDeclararLista,
    origenLista,
    bienesArgentinasLista as bienes_arg_lista,
    bienesExterioresLista as bienes_ext_lista,
)


def configurar_boton_mostrar_datos(ventana):
    boton_mostrar = tk.Button(
        ventana, text="Mostrar Datos", command=accion_mostrar_datos
    )
    boton_mostrar.grid(row=10, column=1, pady=10)


def agregar_boton_salir(ventana):
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.grid(row=11, column=1, pady=10)


def accion_mostrar_datos():
    mostrar_datos(
        dniLista,
        apellidoLista,
        nombreLista,
        edadLista,
        fechaDeNacimientoLista,
        profesionLista,
        montoLista,
        fechaDeclararLista,
        origenLista,
        bienes_arg_lista,
        bienes_ext_lista,
    )
