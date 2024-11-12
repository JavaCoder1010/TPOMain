import tkinter as tk
from tkinter import messagebox
from listas import (
    dniLista,
    apellidoLista,
    edadLista,
    fechaDeclararLista,
    nombreLista,
    fechaDeNacimientoLista,
    profesionLista,
    montoLista,
    origenLista,
    bienesArgentinasLista,
    bienesExterioresLista,
)


def porcentajeDeBienesArgentinos(bienesArgentinasLista, bienesExterioresLista):
    bienesArgentinos = bienesArgentinasLista[0].count(True)
    bienesExteriores = bienesExterioresLista[0].count(True)
    print(bienesArgentinasLista)
    bienestotales = bienesExteriores + bienesArgentinos
    print("Estos son los bienes lista", bienesArgentinos)
    if bienestotales == 0:
        return 0  # Para evitar división por cero
    porcentaje_argentino = (bienesArgentinos / bienestotales) * 100
    return porcentaje_argentino


def porcentajeDeBienesExtranjeros(bienesArgentinasLista, bienesExterioresLista):
    bienesArgentinos = bienesArgentinasLista[0].count(True)
    bienesExteriores = bienesExterioresLista[0].count(True)
    bienestotales = bienesExteriores + bienesArgentinos
    if bienestotales == 0:
        return 0  # Para evitar división por cero
    porcentaje_exterior = (bienesExteriores / bienestotales) * 100
    return porcentaje_exterior


def mostrar_datos(
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
):
    """
    Muestra los datos registrados en una nueva ventana, formateados de manera
    legible. Si no hay datos registrados, muestra un mensaje de advertencia.
    """

    if not dniLista:  # Si no hay datos registrados
        messagebox.showinfo("Sin datos", "No hay datos registrados para mostrar.")
        return

    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Ingresados")

    datos_texto = ""
    lista_datos_texto = []
    for i in range(len(dniLista)):

        datos_texto = (
            f"\nRegistro {i+1}:\n"
            f" DNI: {dniLista[i]}\n"
            f" Apellido: {apellidoLista[i]}\n"
            f" Nombre: {nombreLista[i]}\n"
            f" Edad: {edadLista[i]}\n"
            f" Fecha de Nacimiento: {fechaDeNacimientoLista[i]}\n"
            f" Profesión: {profesionLista[i]}\n"
            f" Monto: {montoLista[i]}\n"
            f" Fecha Declarar: {fechaDeclararLista[i]}\n"
            f" Origen: {origenLista[i]}\n"
            f" Posee {porcentajeDeBienesArgentinos(bienesArgentinasLista, bienesExterioresLista)}% de bienes en argentina y {porcentajeDeBienesExtranjeros(bienesArgentinasLista, bienesExterioresLista)}% en el exterior.\n"
        )

        lista_datos_texto.append(datos_texto)

        # Bienes en Argentina
        bienes_nombres_arg = [
            "Moneda",
            "Inmuebles",
            "Acciones y participaciones",
            "Títulos valores",
            "Otros bienes muebles",
            "Créditos",
            "Derechos y bienes intangibles",
            "Criptomonedas y criptoactivos",
            "Otros bienes",
        ]

        bienes_encontrados_arg = False
        for j, bien in enumerate(bienes_nombres_arg):
            if bienes_arg_lista[i][j]:
                if not bienes_encontrados_arg:
                    datos_texto += " Bienes en Argentina:\n"
                    bienes_encontrados_arg = True
                datos_texto += f" - {bien}\n"

        # Bienes en el exterior
        bienes_nombres_ext = [
            "Moneda extranjera",
            "Inmuebles",
            "Acciones y participaciones",
            "Títulos valores",
            "Otros bienes muebles",
            "Créditos",
            "Derechos y bienes intangibles",
            "Otros bienes",
        ]

        bienes_encontrados_ext = False
        for k, bien in enumerate(bienes_nombres_ext):
            if bienes_ext_lista[i][k]:
                if not bienes_encontrados_ext:
                    datos_texto += " Bienes en el exterior:\n"
                    bienes_encontrados_ext = True
                datos_texto += f" - {bien}\n"

        datos_texto += "-" * 50 + "\n\n"

    # Crear y configurar el área de texto
    text_area = tk.Text(ventana_datos, wrap=tk.WORD, width=80, height=20)
    text_area.insert(tk.END, lista_datos_texto)
    text_area.pack(padx=10, pady=10)

    # Botón para cerrar
    boton_cerrar = tk.Button(
        ventana_datos, text="Cerrar", command=ventana_datos.destroy
    )
    boton_cerrar.pack(pady=10)

    boton_informe = tk.Button(
        ventana_datos, text="Estadísticas", command=generar_estadistica
    )
    boton_informe.pack(pady=20)

    boton_buscar = tk.Button(
        ventana_datos, text="Buscar registro", command=buscar_registro
    )
    boton_buscar.pack(pady=25)


def encontrarmax(edadLista):
    maximo = edadLista[0]
    for edad in edadLista:
        if edad > maximo:
            maximo = edad
    return maximo


def encontrarmin(edadLista):
    minimo = edadLista[0]
    for edad in edadLista:
        if edad < minimo:
            minimo = edad
    return minimo


def promedioedades(edadLista):
    suma = 0
    for edad in edadLista:
        suma += int(edad)
    promedio = suma / len(edadLista)
    return promedio


def generar_estadistica():
    ventana_informe = tk.Toplevel()
    ventana_informe.title("Estadisticas")
    text_area = tk.Text(ventana_informe, wrap=tk.WORD, width=80, height=20)
    cantidad = len(dniLista)
    datos_texto = (
        f"La edad máxima registrada es {encontrarmax(edadLista)}\n"
        f"La edad minima registrada es {encontrarmin(edadLista)}\n"
        f"El promedio de edades regsitradas es de {promedioedades(edadLista)}\n"
        f"La fecha registrada más lejana es {encontrarmin(fechaDeclararLista)}\n"
        f"La cantidad de personas registradas es {cantidad}",
    )

    text_area.insert(tk.END, datos_texto)
    text_area.pack(padx=10, pady=10)
    boton_cerrar = tk.Button(
        ventana_informe, text="Cerrar", command=ventana_informe.destroy
    )
    boton_cerrar.pack(pady=10)


def buscar_registro():
    ventana = tk.Toplevel()
    ventana.title("Buscador de registros")

    etiqueta = tk.Label(
        ventana, text="Para buscar un registro ingrese el DNI del contribuyente:"
    )
    etiqueta.pack(pady=10)

    entrada = tk.Entry(ventana, width=30)
    entrada.pack(pady=5)

    def buscar():
        dnibuscado = entrada.get()
        comparar(dnibuscado)

    boton_buscar = tk.Button(ventana, text="Buscar registro", command=buscar)
    boton_buscar.pack(pady=25)


def comparar(dnibuscado):
    ventana_informe = tk.Toplevel()
    ventana_informe.title("Registros")
    text_area = tk.Text(ventana_informe, wrap=tk.WORD, width=80, height=20)
    int(dnibuscado)
    if dnibuscado in dniLista:
        index = dniLista.index(dnibuscado)
        listadatos = [
            f" DNI: {dniLista[index]}\n"
            f" Apellido: {apellidoLista[index]}\n"
            f" Nombre: {nombreLista[index]}\n"
            f" Edad: {edadLista[index]}\n"
            f" Fecha de Nacimiento: {fechaDeNacimientoLista[index]}\n"
            f" Profesión: {profesionLista[index]}\n"
            f" Monto: {montoLista[index]}\n"
            f" Fecha Declarar: {fechaDeclararLista[index]}\n"
            f" Origen: {origenLista[index]}\n"
        ]
        datos_texto = listadatos
    else:
        datos_texto = "No se encontró el DNI ingresado."

    text_area.insert(tk.END, datos_texto)
    text_area.pack(padx=10, pady=10)
    boton_cerrar = tk.Button(
        ventana_informe, text="Cerrar", command=ventana_informe.destroy
    )
    boton_cerrar.pack(pady=10)
