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


def contar_activos_regularizados(bienesArgentinasLista, bienesExterioresLista):
    """
    Cuenta la frecuencia de cada activo regularizado.
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

    # Inicializar contadores
    conteo_bienes = {}

    # Contar bienes en Argentina
    for i in range(len(bienesArgentinasLista)):
        for j, bien in enumerate(bienes_nombres_arg):
            if bienesArgentinasLista[i][j]:
                if bien in conteo_bienes:
                    conteo_bienes[bien] += 1
                else:
                    conteo_bienes[bien] = 1

    # Contar bienes en el exterior
    for i in range(len(bienesExterioresLista)):
        for j, bien in enumerate(bienes_nombres_ext):
            if bienesExterioresLista[i][j]:
                if bien in conteo_bienes:
                    conteo_bienes[bien] += 1
                else:
                    conteo_bienes[bien] = 1

    return conteo_bienes


def generar_ranking_profesiones(profesionLista):
    """
    Genera un ranking de profesiones ordenado por frecuencia.
    Implementación usando solo listas y operaciones básicas.
    """
    # Listas paralelas para profesiones únicas y sus conteos
    profesiones_unicas = []
    conteos = []
    
    # Contamos ocurrencias
    for profesion in profesionLista:
        encontrado = False
        for i in range(len(profesiones_unicas)):
            if profesiones_unicas[i] == profesion:
                conteos[i] += 1
                encontrado = True
                break
        if not encontrado:
            profesiones_unicas.append(profesion)
            conteos.append(1)
    
    # Ordenamiento burbuja por conteos
    n = len(profesiones_unicas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if conteos[j] < conteos[j + 1]:
                conteos[j], conteos[j + 1] = conteos[j + 1], conteos[j]
                profesiones_unicas[j], profesiones_unicas[j + 1] = profesiones_unicas[j + 1], profesiones_unicas[j]
    
    # Construimos el ranking final
    ranking = []
    for i in range(len(profesiones_unicas)):
        ranking.append((profesiones_unicas[i], conteos[i]))
        
    return ranking


def generar_ranking_origen(origenLista):
    """
    Genera un ranking del origen de los fondos ordenado por frecuencia.
    Implementación sin usar diccionarios ni funciones integradas.
    """
    # LISTAS PARALELAS PARA CONTAR
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
                # Intercambiamos tanto conteos como orígenes
                conteos[j], conteos[j + 1] = conteos[j + 1], conteos[j]
                origenes_unicos[j], origenes_unicos[j + 1] = origenes_unicos[j + 1], origenes_unicos[j]
    
    # Generamos el ranking final como lista de tuplas
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
    Muestra los datos registrados en una nueva ventana.
    """
    if not dniLista:
        messagebox.showinfo("Sin datos", "No hay datos registrados para mostrar.")
        return

    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Ingresados")

    datos_texto = ""
    lista_datos_texto = []
    for i in range(len(dniLista)):
        # Calculamos los porcentajes para este registro específico
        porcentaje_arg = porcentajeDeBienesArgentinos(
            bienes_arg_lista, bienes_ext_lista, i
        )
        porcentaje_ext = porcentajeDeBienesExtranjeros(
            bienes_arg_lista, bienes_ext_lista, i
        )

        datos_texto = (
            f"\nRegistro {i+1}:\n"
            f" DNI: {dniLista[i]}\n"
            f" Apellido: {apellidoLista[i]}\n"
            f" Nombre: {nombreLista[i]}\n"
            f" Edad: {edadLista[i]}\n"
            f" Fecha de Nacimiento: {fechaDeNacimientoLista[i]}\n"
            f" Profesión: {profesionLista[i]}\n"
            f" Monto: {montoLista[i]:,.2f}\n"
            f" Fecha Declarar: {fechaDeclararLista[i]}\n"
            f" Origen: {origenLista[i]}\n"
            f" Posee {porcentaje_arg:.1f}% de bienes en argentina y {porcentaje_ext:.1f}% en el exterior.\n"
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
    # 1. Crear ventana nueva para mostrar estadísticas
    ventana_informe = tk.Toplevel()
    ventana_informe.title("Estadísticas")
    text_area = tk.Text(ventana_informe, wrap=tk.WORD, width=80, height=30)

    # 2. Calcular cantidad de registros
    cantidad_registros = 0
    for dni in dniLista:
        cantidad_registros = cantidad_registros + 1

    # 3. Contar todos los bienes (Argentina y exterior) para calcular porcentajes
    total_bienes_arg = 0
    total_bienes_ext = 0

    # 3.1 Contar bienes en Argentina para todos los registros
    for lista_bienes in bienesArgentinasLista:
        for bien in lista_bienes:
            if bien == True:
                total_bienes_arg = total_bienes_arg + 1

    # 3.2 Contar bienes en el exterior para todos los registros
    for lista_bienes in bienesExterioresLista:
        for bien in lista_bienes:
            if bien == True:
                total_bienes_ext = total_bienes_ext + 1

    # 3.3 Calcular porcentajes
    total_bienes = total_bienes_arg + total_bienes_ext
    if total_bienes > 0:
        porcentaje_arg = (total_bienes_arg * 100) / total_bienes
        porcentaje_ext = (total_bienes_ext * 100) / total_bienes
    else:
        porcentaje_arg = 0
        porcentaje_ext = 0

    # 4. Crear lista de todos los activos y contar frecuencias
    # 4.1 Definir nombres de bienes
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

    # 4.2 Crear lista para almacenar [nombre_activo, cantidad]
    conteo_activos = []

    # 4.3 Contar bienes en Argentina
    for i in range(len(bienes_nombres_arg)):
        cantidad = 0
        for registro in bienesArgentinasLista:
            if registro[i] == True:
                cantidad = cantidad + 1
        if cantidad > 0:
            conteo_activos.append([bienes_nombres_arg[i], cantidad])

    # 4.4 Contar bienes en el exterior
    for i in range(len(bienes_nombres_ext)):
        cantidad = 0
        for registro in bienesExterioresLista:
            if registro[i] == True:
                cantidad = cantidad + 1
        if cantidad > 0:
            conteo_activos.append([bienes_nombres_ext[i], cantidad])

    # 4.5 Ordenar activos por cantidad (orden descendente)
    conteo_activos_ordenados = []
    while len(conteo_activos) > 0:
        indice_maximo = 0
        for i in range(len(conteo_activos)):
            if conteo_activos[i][1] > conteo_activos[indice_maximo][1]:
                indice_maximo = i
        conteo_activos_ordenados.append(conteo_activos[indice_maximo])
        conteo_activos.pop(indice_maximo)

    # 5. Determinar activo más y menos común
    if len(conteo_activos_ordenados) > 0:
        activo_mas_comun = conteo_activos_ordenados[0]
        activo_menos_comun = conteo_activos_ordenados[len(conteo_activos_ordenados) - 1]
    else:
        activo_mas_comun = ["Ninguno", 0]
        activo_menos_comun = ["Ninguno", 0]

    # 6. Contar frecuencia de profesiones
    profesiones_conteo = []
    for profesion in profesionLista:
        # 6.1 Buscar si la profesión ya está en la lista
        encontrada = False
        for i in range(len(profesiones_conteo)):
            if profesiones_conteo[i][0] == profesion:
                profesiones_conteo[i][1] = profesiones_conteo[i][1] + 1
                encontrada = True
                break
        # 6.2 Si no está, agregarla
        if not encontrada:
            profesiones_conteo.append([profesion, 1])

    # 6.3 Ordenar profesiones por cantidad (orden descendente)
    ranking_profesiones = []
    while len(profesiones_conteo) > 0:
        indice_maximo = 0
        for i in range(len(profesiones_conteo)):
            if profesiones_conteo[i][1] > profesiones_conteo[indice_maximo][1]:
                indice_maximo = i
        ranking_profesiones.append(profesiones_conteo[indice_maximo])
        profesiones_conteo.pop(indice_maximo)

    # 7. Contar frecuencia de orígenes de fondos
    origenes_conteo = []
    for origen in origenLista:
        # 7.1 Buscar si el origen ya está en la lista
        encontrado = False
        for i in range(len(origenes_conteo)):
            if origenes_conteo[i][0] == origen:
                origenes_conteo[i][1] = origenes_conteo[i][1] + 1
                encontrado = True
                break
        # 7.2 Si no está, agregarlo
        if not encontrado:
            origenes_conteo.append([origen, 1])

    # 7.3 Ordenar orígenes por cantidad (orden descendente)
    ranking_origen = []
    while len(origenes_conteo) > 0:
        indice_maximo = 0
        for i in range(len(origenes_conteo)):
            if origenes_conteo[i][1] > origenes_conteo[indice_maximo][1]:
                indice_maximo = i
        ranking_origen.append(origenes_conteo[indice_maximo])
        origenes_conteo.pop(indice_maximo)

    # 8. Construir texto de estadísticas
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
        datos_texto + f"- Fecha más lejana: {encontrarmin(fechaDeclararLista)}\n"
    )
    datos_texto = (
        datos_texto + f"- Fecha más cercana: {encontrarmax(fechaDeclararLista)}\n\n"
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

    # 9. Mostrar resultados en la ventana
    text_area.insert(tk.END, datos_texto)
    text_area.pack(padx=10, pady=10)

    # 10. Agregar scrollbar
    scrollbar = tk.Scrollbar(ventana_informe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)

    # 11. Agregar botón para cerrar
    boton_cerrar = tk.Button(
        ventana_informe, text="Cerrar", command=ventana_informe.destroy
    )
    boton_cerrar.pack(pady=10)


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
    # 1. Crear la ventana de informe
    ventana_informe = tk.Toplevel()
    ventana_informe.title("Registros")

    # 2. Crear el área de texto
    text_area = tk.Text(ventana_informe, wrap=tk.WORD, width=80, height=20)

    # 3. Buscar el DNI en la lista
    encontrado = False
    indice = 0

    # Buscar el índice del DNI manualmente
    for i in range(len(dniLista)):
        if dniLista[i] == dnibuscado:
            encontrado = True
            indice = i
            break

    # 4. Si encontramos el DNI, procesar la información
    if encontrado:
        # 4.1 Calcular porcentajes de bienes
        total_bienes_arg = 0
        total_bienes_ext = 0

        # Contar bienes en Argentina
        for bien in bienesArgentinasLista[indice]:
            if bien:
                total_bienes_arg = total_bienes_arg + 1

        # Contar bienes en el exterior
        for bien in bienesExterioresLista[indice]:
            if bien:
                total_bienes_ext = total_bienes_ext + 1

        # Calcular porcentajes
        total_bienes = total_bienes_arg + total_bienes_ext
        if total_bienes > 0:
            porcentaje_arg = (total_bienes_arg * 100) / total_bienes
            porcentaje_ext = (total_bienes_ext * 100) / total_bienes
        else:
            porcentaje_arg = 0
            porcentaje_ext = 0

        # 4.2 Construir el texto con la información básica
        texto_resultado = []
        texto_resultado.append(f" DNI: {dniLista[indice]}\n")
        texto_resultado.append(f" Apellido: {apellidoLista[indice]}\n")
        texto_resultado.append(f" Nombre: {nombreLista[indice]}\n")
        texto_resultado.append(f" Edad: {edadLista[indice]}\n")
        texto_resultado.append(
            f" Fecha de Nacimiento: {fechaDeNacimientoLista[indice]}\n"
        )
        texto_resultado.append(f" Profesión: {profesionLista[indice]}\n")

        # Formatear el monto manualmente
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

        # 4.3 Agregar información de bienes en Argentina
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

        # 4.4 Agregar información de bienes en el exterior
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

    # 5. Si no encontramos el DNI, mostrar mensaje de error
    else:
        texto_resultado = ["No se encontró el DNI ingresado."]

    # 6. Insertar el texto en el área de texto
    texto_final = ""
    for linea in texto_resultado:
        texto_final = texto_final + linea

    text_area.insert(tk.END, texto_final)

    # 7. Configurar scrollbar
    scrollbar = tk.Scrollbar(ventana_informe)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_area.yview)

    # 8. Agregar el área de texto y el botón de cerrar a la ventana
    text_area.pack(padx=10, pady=10)
    boton_cerrar = tk.Button(
        ventana_informe, text="Cerrar", command=ventana_informe.destroy
    )
    boton_cerrar.pack(pady=10)
