from generar_estadistica import generar_estadistica
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


def porcentajeDeBienesArgentinos(bienesArgentinasLista, bienesExterioresLista, indice):
    """
    Calcula el porcentaje de bienes en Argentina para un registro específico.

    Args:
        bienesArgentinasLista (list): Lista de bienes en Argentina
        bienesExterioresLista (list): Lista de bienes en el exterior
        indice (int): Índice del registro actual
    """
    bienesArgentinos = 0
    for valor in bienesArgentinasLista[indice]:
        if valor:
            bienesArgentinos += 1

    bienesExteriores = 0
    for valor in bienesExterioresLista[indice]:
        if valor:
            bienesExteriores += 1

    bienestotales = bienesExteriores + bienesArgentinos

    if bienestotales == 0:
        return 0  # Para evitar división por cero

    porcentaje_argentino = (bienesArgentinos / bienestotales) * 100
    return porcentaje_argentino


def porcentajeDeBienesExtranjeros(bienesArgentinasLista, bienesExterioresLista, indice):
    """
    Calcula el porcentaje de bienes en el exterior para un registro específico.
    """
    bienesArgentinos = 0
    for valor in bienesArgentinasLista[indice]:
        if valor:
            bienesArgentinos += 1

    bienesExteriores = 0
    for valor in bienesExterioresLista[indice]:
        if valor:
            bienesExteriores += 1

    bienestotales = bienesExteriores + bienesArgentinos

    if bienestotales == 0:
        return 0  # Para evitar división por cero

    porcentaje_exterior = (bienesExteriores / bienestotales) * 100
    return porcentaje_exterior


def contar_bien_especifico(lista_registros, indice):
    """
    Cuenta cuántas veces aparece un bien específico en una lista de registros
    """
    cantidad = 0
    for registro in lista_registros:
        if registro[indice] == True:
            cantidad = cantidad + 1
    return cantidad


def agregar_bien_a_conteo(conteo_bienes, nombre_bien, cantidad):
    """
    Agrega o actualiza la cantidad de un bien en la lista de conteo
    """
    if cantidad == 0:
        return conteo_bienes

    for i in range(len(conteo_bienes)):
        if conteo_bienes[i][0] == nombre_bien:
            conteo_bienes[i][1] = conteo_bienes[i][1] + cantidad
            return conteo_bienes

    conteo_bienes.append([nombre_bien, cantidad])
    return conteo_bienes


def ordenar_conteo_descendente(conteo_bienes):
    """
    Ordena la lista de conteo de mayor a menor cantidad
    """
    for i in range(len(conteo_bienes)):
        for j in range(len(conteo_bienes) - 1 - i):
            if conteo_bienes[j][1] < conteo_bienes[j + 1][1]:
                temp = conteo_bienes[j]
                conteo_bienes[j] = conteo_bienes[j + 1]
                conteo_bienes[j + 1] = temp
    return conteo_bienes


def contar_activos_regularizados(bienesArgentinasLista, bienesExterioresLista):
    """
    Cuenta la frecuencia de cada activo regularizado.
    Retorna una lista de listas donde cada elemento contiene [nombre_bien, cantidad]
    """
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

    conteo_bienes = []

    for i in range(len(bienes_nombres_arg)):
        nombre_bien = bienes_nombres_arg[i]
        cantidad = contar_bien_especifico(bienesArgentinasLista, i)
        conteo_bienes = agregar_bien_a_conteo(conteo_bienes, nombre_bien, cantidad)

    for i in range(len(bienes_nombres_ext)):
        nombre_bien = bienes_nombres_ext[i]
        cantidad = contar_bien_especifico(bienesExterioresLista, i)
        conteo_bienes = agregar_bien_a_conteo(conteo_bienes, nombre_bien, cantidad)

    conteo_bienes = ordenar_conteo_descendente(conteo_bienes)

    return conteo_bienes


def generar_ranking_profesiones(profesionLista):
    """
    Genera un ranking de profesiones ordenado por frecuencia.
    Retorna una lista donde cada elemento es [profesion, cantidad]
    ordenada de mayor a menor frecuencia.
    """

    ranking = []

    for profesion in profesionLista:
        encontrado = False
        for i in range(len(ranking)):
            if ranking[i][0] == profesion:
                ranking[i][1] = ranking[i][1] + 1
                encontrado = True
                break

        if encontrado == False:
            nueva_profesion = [profesion, 1]
            ranking.append(nueva_profesion)

    for i in range(len(ranking)):
        for j in range(len(ranking) - 1 - i):
            if ranking[j][1] < ranking[j + 1][1]:
                temp = ranking[j]
                ranking[j] = ranking[j + 1]
                ranking[j + 1] = temp

    return ranking


def generar_ranking_origen(origenLista):
    """
    Genera un ranking del origen de los fondos ordenado por frecuencia.
    Implementación sin usar diccionarios ni funciones integradas.
    """
    origenes_unicos = []
    conteos = []

    for origen in origenLista:
        encontrado = False
        for i in range(len(origenes_unicos)):
            if origenes_unicos[i] == origen:
                conteos[i] += 1
                encontrado = True
                break
        if not encontrado:
            origenes_unicos.append(origen)
            conteos.append(1)

    # Ordenamiento burbuja por conteos
    n = len(origenes_unicos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if conteos[j] < conteos[j + 1]:
                conteos[j], conteos[j + 1] = conteos[j + 1], conteos[j]
                origenes_unicos[j], origenes_unicos[j + 1] = (
                    origenes_unicos[j + 1],
                    origenes_unicos[j],
                )

    ranking = []
    for i in range(len(origenes_unicos)):
        ranking.append((origenes_unicos[i], conteos[i]))

    return ranking


def calcular_porcentaje_total_bienes(bienesArgentinasLista, bienesExterioresLista):
    """
    Calcula el porcentaje total de bienes en Argentina y en el exterior.
    """
    total_arg = 0
    total_ext = 0
    total_bienes = 0

    for i in range(len(bienesArgentinasLista)):
        bienes_arg = 0
        for valor in bienesArgentinasLista[i]:
            if valor:
                bienes_arg += 1

        bienes_ext = 0
        for valor in bienesExterioresLista[i]:
            if valor:
                bienes_ext += 1
        total_arg += bienes_arg
        total_ext += bienes_ext
        total_bienes += bienes_arg + bienes_ext

    if total_bienes == 0:
        return 0, 0

    porcentaje_arg = (total_arg / total_bienes) * 100
    porcentaje_ext = (total_ext / total_bienes) * 100

    return porcentaje_arg, porcentaje_ext


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
    Muestra los datos registrados en una nueva ventana con formato simplificado.
    """
    if not dniLista:
        messagebox.showinfo("Sin datos", "No hay datos registrados para mostrar.")
        return

    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Ingresados")

    ancho_etiqueta = 25
    linea_separadora = "=" * 50
    linea_sencilla = "-" * 40
    lista_datos_completa = []

    for i in range(len(dniLista)):
        porcentaje_arg = porcentajeDeBienesArgentinos(
            bienes_arg_lista, bienes_ext_lista, i
        )
        porcentaje_ext = porcentajeDeBienesExtranjeros(
            bienes_arg_lista, bienes_ext_lista, i
        )

        fecha_nacimiento = fechaDeNacimientoLista[i].strftime("%Y-%m-%d")
        fecha_declarar = fechaDeclararLista[i].strftime("%Y-%m-%d")

        datos_registro = (
            f"\n{linea_separadora}\n"
            f"REGISTRO {i+1}\n"
            f"{linea_sencilla}\n"
            f"{'DNI:':<{ancho_etiqueta}} {dniLista[i]}\n"
            f"{'Apellido:':<{ancho_etiqueta}} {apellidoLista[i]}\n"
            f"{'Nombre:':<{ancho_etiqueta}} {nombreLista[i]}\n"
            f"{'Edad:':<{ancho_etiqueta}} {edadLista[i]}\n"
            f"{'Fecha de Nacimiento:':<{ancho_etiqueta}} {fecha_nacimiento}\n"
            f"{'Profesión:':<{ancho_etiqueta}} {profesionLista[i]}\n"
            f"{'Monto:':<{ancho_etiqueta}} ${montoLista[i]:,.2f}\n"
            f"{'Fecha en la que se declaró:':<{ancho_etiqueta}} {fecha_declarar}\n"
            f"{'Origen:':<{ancho_etiqueta}} {origenLista[i]}\n"
            f"{'Bienes en Argentina:':<{ancho_etiqueta}} {porcentaje_arg:.1f}%\n"
            f"{'Bienes en el Exterior:':<{ancho_etiqueta}} {porcentaje_ext:.1f}%\n"
        )

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
                    datos_registro += "\nBienes en Argentina:\n"
                    datos_registro += "-" * 40 + "\n"
                    bienes_encontrados_arg = True
                datos_registro += f"  • {bien}\n"

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
                    datos_registro += "\nBienes en el Exterior:\n"
                    datos_registro += "-" * 40 + "\n"
                    bienes_encontrados_ext = True
                datos_registro += f"  • {bien}\n"

        datos_registro += f"\n{linea_separadora}\n"
        lista_datos_completa.append(datos_registro)

    text_area = tk.Text(ventana_datos, wrap=tk.WORD, width=80, height=30)
    text_area.insert(tk.END, "".join(lista_datos_completa))
    text_area.pack(padx=10, pady=10)

    frame_botones = tk.Frame(ventana_datos)
    frame_botones.pack(pady=10)

    boton_cerrar = tk.Button(
        frame_botones, text="Cerrar", command=ventana_datos.destroy
    )
    boton_cerrar.pack(side=tk.LEFT, padx=5)

    boton_informe = tk.Button(
        frame_botones, text="Estadísticas", command=generar_estadistica
    )
    boton_informe.pack(side=tk.LEFT, padx=5)

    boton_buscar = tk.Button(
        frame_botones, text="Buscar registro", command=buscar_registro
    )
    boton_buscar.pack(side=tk.LEFT, padx=5)


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


def buscar_registro():
    """
    Crea una ventana para buscar un registro por DNI.
    """
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
    """
    Muestra los detalles de un registro específico basado en el DNI.
    Args:
        dnibuscado (str): DNI a buscar en los registros
    """
    ventana_informe = tk.Toplevel()
    ventana_informe.title("Registros")

    text_area = tk.Text(ventana_informe, wrap=tk.WORD, width=80, height=20)

    encontrado = False
    indice = 0

    for i in range(len(dniLista)):
        if dniLista[i] == dnibuscado:
            encontrado = True
            indice = i
            break

    if encontrado:
        total_bienes_arg = 0
        total_bienes_ext = 0

        for bien in bienesArgentinasLista[indice]:
            if bien:
                total_bienes_arg = total_bienes_arg + 1

        for bien in bienesExterioresLista[indice]:
            if bien:
                total_bienes_ext = total_bienes_ext + 1

        total_bienes = total_bienes_arg + total_bienes_ext
        if total_bienes > 0:
            porcentaje_arg = (total_bienes_arg * 100) / total_bienes
            porcentaje_ext = (total_bienes_ext * 100) / total_bienes
        else:
            porcentaje_arg = 0
            porcentaje_ext = 0

        texto_resultado = []
        texto_resultado.append(f" DNI: {dniLista[indice]}\n")
        texto_resultado.append(f" Apellido: {apellidoLista[indice]}\n")
        texto_resultado.append(f" Nombre: {nombreLista[indice]}\n")
        texto_resultado.append(f" Edad: {edadLista[indice]}\n")
        texto_resultado.append(
            f" Fecha de Nacimiento: {fechaDeNacimientoLista[indice]}\n"
        )
        texto_resultado.append(f" Profesión: {profesionLista[indice]}\n")

        monto = montoLista[indice]
        monto_texto = ""
        monto_str = str(int(monto))
        contador = 0
        for i in range(len(monto_str) - 1, -1, -1):
            if contador == 3:
                monto_texto = "," + monto_texto
                contador = 0
            monto_texto = monto_str[i] + monto_texto
            contador = contador + 1

        texto_resultado.append(f" Monto: ${monto_texto}.00\n")
        texto_resultado.append(f" Fecha Declarar: {fechaDeclararLista[indice]}\n")
        texto_resultado.append(f" Origen: {origenLista[indice]}\n")
        texto_resultado.append(
            f" Posee {porcentaje_arg:.1f}% de bienes en argentina y {porcentaje_ext:.1f}% en el exterior.\n"
        )

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

        texto_resultado.append("\nBienes en Argentina:\n")
        tiene_bienes_arg = False

        for i in range(len(bienes_nombres_arg)):
            if bienesArgentinasLista[indice][i]:
                texto_resultado.append(f" - {bienes_nombres_arg[i]}\n")
                tiene_bienes_arg = True

        if not tiene_bienes_arg:
            texto_resultado.append(" Ninguno\n")

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

        texto_resultado.append("\nBienes en el exterior:\n")
        tiene_bienes_ext = False

        for i in range(len(bienes_nombres_ext)):
            if bienesExterioresLista[indice][i]:
                texto_resultado.append(f" - {bienes_nombres_ext[i]}\n")
                tiene_bienes_ext = True

        if not tiene_bienes_ext:
            texto_resultado.append(" Ninguno\n")

    else:
        texto_resultado = ["No se encontró el DNI ingresado."]

    texto_final = ""
    for linea in texto_resultado:
        texto_final = texto_final + linea

    text_area.insert(tk.END, texto_final)

    scrollbar = tk.Scrollbar(ventana_informe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)

    text_area.pack(padx=10, pady=10)
    boton_cerrar = tk.Button(
        ventana_informe, text="Cerrar", command=ventana_informe.destroy
    )
    boton_cerrar.pack(pady=10)
