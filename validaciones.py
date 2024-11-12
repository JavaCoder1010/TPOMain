from datetime import datetime


def separar_por_guiones(fecha_str):
    """
    Separa una cadena de texto que representa una fecha en sus componentes
    individuales (día, mes y año).

    La función itera sobre la cadena de texto y cada vez que encuentra un carácter
    '-' (guion), agrega la parte actual a la lista de componentes y reinicia la
    parte. Al final, agrega la parte actual a la lista.

    Esta función es usada como parte de la función es_fecha_valida, que verifica
    si una fecha dada como cadena tiene un formato válido y corresponde a una
    fecha real.

    Args:
        fecha_str (str): La fecha como cadena de texto, con componentes separados
            por guiones.

    Returns:
        list: La lista de componentes individuales de la fecha, en el orden
            'día', 'mes', 'año'.
    """
    componentes = []
    parte = ""

    for caracter in fecha_str:
        if caracter == "-":
            componentes.append(parte)
            parte = ""
        else:
            parte += caracter

    componentes.append(parte)
    return componentes


def es_fecha_valida(fecha_str, formato="%d-%m-%Y"):
    """
    Verifica si una fecha dada como cadena tiene un formato válido y corresponde
    a una fecha real. El formato por defecto es 'dd-mm-aaaa'.

    Args:
        fecha_str (str): La fecha como cadena de texto, con componentes separados
            por guiones.
        formato (str): El formato esperado de la fecha. Actualmente, solo el
            formato '%d-%m-%Y' es soportado.

    Nota:
        - Este método verifica que el día, mes y año sean números y que la fecha
          esté dentro de un rango razonable (año actual más o menos 100 años).
        - Se consideran los años bisiestos al validar febrero.
    """
    if formato == "%d-%m-%Y":
        componentes = separar_por_guiones(fecha_str)
        if len(componentes) != 3:
            return False
        dia_str, mes_str, año_str = componentes
        for s in [dia_str, mes_str, año_str]:
            for c in s:
                if c < "0" or c > "9":
                    return False

        dia = int(dia_str)
        mes = int(mes_str)
        año = int(año_str)

        hoy = datetime.today()
        if año < hoy.year - 100 or año > hoy.year + 5:
            return False
        if 1 <= mes <= 12:
            # Días en cada mes, sin considerar bisiestos
            dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            # Años bisiestos
            if mes == 2:
                if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
                    dias_por_mes[1] = 29
            ultimo_dia = dias_por_mes[mes - 1]
            if 1 <= dia <= ultimo_dia:
                return True
    return False


def es_dni_valido(dni):
    """
    Verifica si el DNI es válido, siendo la longitud entre 7 y 9 caracteres.
    """
    longitud_dni = 0
    for caracter in dni:
        longitud_dni += 1
    if longitud_dni < 7 or longitud_dni > 9:
        return False

    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    indice = 0
    for caracter in dni:
        if indice == longitud_dni - 1:
            break
        es_numero = False
        for numero in numeros:
            if caracter == numero:
                es_numero = True
                break
        if not es_numero:
            return False
        indice += 1

    return True


def es_string_valido(campo):
    # Verificar si el campo está vacío o contiene solo espacios en blanco
    """
    Verifica si un campo de texto es válido.

    Un campo de texto es válido si no está vacío, contiene solo espacios en blanco, es de tipo string y todos sus caracteres son letras.
    """
    es_vacio = True
    for caracter in campo:
        if caracter != " ":
            es_vacio = False
            break
    if es_vacio:
        return False

    # Verificar si el campo es de tipo string
    es_string = False
    if type(campo) == str:
        es_string = True
    else:
        return False

    letras_mayusculas = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "Ñ",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    letras_minusculas = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "ñ",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    # Verificar que todos los caracteres sean letras
    for caracter in campo:
        es_letra = False
        for letra in letras_mayusculas:
            if caracter == letra:
                es_letra = True
                break

        for letra in letras_minusculas:
            if caracter == letra:
                es_letra = True
                break

        if not es_letra:
            return False

    return True


def es_edad_valida(edad):
    """
    Verifica si una edad dada como cadena de texto es válida.

    Una edad es válida si no está vacía, contiene solo caracteres numéricos,
    y se encuentra dentro del rango de 18 a 100 años.
    """
    es_vacia = True
    for caracter in edad:
        if caracter != " ":
            es_vacia = False
            break
    if es_vacia:
        return False

    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    es_numero = True
    for caracter in edad:
        es_caracter_valido = False
        for numero in numeros:
            if caracter == numero:
                es_caracter_valido = True
                break
        if not es_caracter_valido:
            es_numero = False
            break

    if not es_numero:
        return False

    # Convertir la edad a entero manualmente
    edad_entero = 0
    for caracter in edad:
        edad_entero = edad_entero * 10  # Desplazamos el dígito
        for i, numero in enumerate(numeros):
            if caracter == numero:
                edad_entero += i
                break

    # Validar el rango de edad
    if edad_entero < 18 or edad_entero > 100:
        return False

    return True
