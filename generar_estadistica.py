import tkinter as tk
from listas import (
    dniLista,
    edadLista,
    fechaDeclararLista,
    montoLista,
    profesionLista,
    origenLista,
    bienesArgentinasLista,
    bienesExterioresLista,
)


def encontrarmax(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo


def encontrarmin(lista):
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo


def promedioedades(lista):
    suma = 0
    for elemento in lista:
        suma += int(elemento)
    promedio = suma / len(lista)
    return promedio


def contar_registros(lista):
    contador = 0
    for elemento in lista:
        contador = contador + 1
    return contador


def contar_bienes(lista_de_listas):
    total = 0
    for lista in lista_de_listas:
        for bien in lista:
            if bien == True:
                total = total + 1
    return total


def calcular_porcentaje(parte, total):
    if total > 0:
        return (parte * 100) / total
    return 0


def contar_tipos_bienes(lista_nombres, lista_registros):
    conteo = []
    for i in range(len(lista_nombres)):
        cantidad = 0
        for registro in lista_registros:
            if registro[i] == True:
                cantidad = cantidad + 1
        if cantidad > 0:
            conteo.append([lista_nombres[i], cantidad])
    return conteo


def ordenar_lista_descendente(lista):
    lista_ordenada = []
    lista_trabajo = lista.copy()
    while len(lista_trabajo) > 0:
        indice_maximo = 0
        for i in range(len(lista_trabajo)):
            if lista_trabajo[i][1] > lista_trabajo[indice_maximo][1]:
                indice_maximo = i
        lista_ordenada.append(lista_trabajo[indice_maximo])
        lista_trabajo.pop(indice_maximo)
    return lista_ordenada


def contar_frecuencias(lista):
    conteo = []
    for elemento in lista:
        encontrado = False
        for i in range(len(conteo)):
            if conteo[i][0] == elemento:
                conteo[i][1] = conteo[i][1] + 1
                encontrado = True
                break
        if not encontrado:
            conteo.append([elemento, 1])
    return conteo


def generar_estadistica():
    ventana_informe = tk.Toplevel()
    ventana_informe.title("Estadísticas")
    text_area = tk.Text(ventana_informe, wrap=tk.WORD, width=80, height=30)

    # Conteos básicos
    cantidad_registros = contar_registros(dniLista)
    total_bienes_arg = contar_bienes(bienesArgentinasLista)
    total_bienes_ext = contar_bienes(bienesExterioresLista)

    # Cálculo de porcentajes
    total_bienes = total_bienes_arg + total_bienes_ext
    porcentaje_arg = calcular_porcentaje(total_bienes_arg, total_bienes)
    porcentaje_ext = calcular_porcentaje(total_bienes_ext, total_bienes)

    # Definición de tipos de bienes
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

    # Conteo de activos
    conteo_arg = contar_tipos_bienes(bienes_nombres_arg, bienesArgentinasLista)
    conteo_ext = contar_tipos_bienes(bienes_nombres_ext, bienesExterioresLista)
    conteo_activos = conteo_arg + conteo_ext
    conteo_activos_ordenados = ordenar_lista_descendente(conteo_activos)

    # Determinación de activos más y menos comunes
    if len(conteo_activos_ordenados) > 0:
        activo_mas_comun = conteo_activos_ordenados[0]
        activo_menos_comun = conteo_activos_ordenados[-1]
    else:
        activo_mas_comun = ["Ninguno", 0]
        activo_menos_comun = ["Ninguno", 0]

    # Rankings
    ranking_profesiones = ordenar_lista_descendente(contar_frecuencias(profesionLista))
    ranking_origen = ordenar_lista_descendente(contar_frecuencias(origenLista))

    # Generación del informe
    datos_texto = ""
    datos_texto = datos_texto + "ESTADÍSTICAS GENERALES:\n"
    datos_texto = datos_texto + "----------------------\n"
    datos_texto = (
        datos_texto + f"Cantidad de personas registradas: {cantidad_registros}\n\n"
    )

    datos_texto = datos_texto + "EDADES:\n"
    datos_texto = datos_texto + f"- Edad máxima: {encontrarmax(edadLista)} años\n"
    datos_texto = datos_texto + f"- Edad mínima: {encontrarmin(edadLista)} años\n"
    datos_texto = (
        datos_texto + f"- Edad promedio: {promedioedades(edadLista):.1f} años\n\n"
    )

    datos_texto = datos_texto + "MONTOS:\n"
    datos_texto = datos_texto + f"- Monto máximo: ${encontrarmax(montoLista):,.2f}\n"
    datos_texto = datos_texto + f"- Monto mínimo: ${encontrarmin(montoLista):,.2f}\n"
    datos_texto = (
        datos_texto + f"- Monto promedio: ${promedioedades(montoLista):,.2f}\n\n"
    )

    datos_texto = datos_texto + "FECHAS DE DECLARACIÓN:\n"
    datos_texto = (
        datos_texto + f"- Fecha más lejana: {encontrarmin(fechaDeclararLista).date()}\n"
    )
    datos_texto = (
        datos_texto
        + f"- Fecha más cercana: {encontrarmax(fechaDeclararLista).date()}\n\n"
    )

    datos_texto = (
        datos_texto + "BIENES TOTALES DECLARADOS DE TODOS LOS CONTRIBUYENTES:\n"
    )
    datos_texto = datos_texto + f"- En Argentina: {porcentaje_arg:.1f}%\n"
    datos_texto = datos_texto + f"- En el exterior: {porcentaje_ext:.1f}%\n\n"

    datos_texto = datos_texto + "ACTIVOS REGULARIZADOS:\n"
    datos_texto = (
        datos_texto
        + f"- Más común: {activo_mas_comun[0]} ({activo_mas_comun[1]} veces)\n"
    )
    datos_texto = (
        datos_texto
        + f"- Menos común: {activo_menos_comun[0]} ({activo_menos_comun[1]} veces)\n\n"
    )

    datos_texto = datos_texto + "RANKING DE PROFESIONES:\n"
    for i in range(len(ranking_profesiones)):
        numero = i + 1
        profesion = ranking_profesiones[i][0]
        cantidad = ranking_profesiones[i][1]
        datos_texto = datos_texto + f"{numero}. {profesion}: {cantidad} personas\n"

    datos_texto = datos_texto + "\nRANKING DE ORIGEN DE FONDOS:\n"
    for i in range(len(ranking_origen)):
        numero = i + 1
        origen = ranking_origen[i][0]
        cantidad = ranking_origen[i][1]
        datos_texto = datos_texto + f"{numero}. {origen}: {cantidad} registros\n"

    # Configuración de la interfaz
    text_area.insert(tk.END, datos_texto)
    text_area.pack(padx=10, pady=10)

    scrollbar = tk.Scrollbar(ventana_informe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)

    boton_cerrar = tk.Button(
        ventana_informe, text="Cerrar", command=ventana_informe.destroy
    )
    boton_cerrar.pack(pady=10)
