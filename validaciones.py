from datetime import datetime

def separar_por_guiones(fecha_str):
    componentes = []
    parte = ''
    
    for caracter in fecha_str:
        if caracter == '-':
            componentes.append(parte)
            parte = ''
        else:
            parte += caracter
    
    componentes.append(parte)
    return componentes

def es_fecha_valida(fecha_str, formato='%d-%m-%Y'):
    if formato == '%d-%m-%Y':
        componentes = separar_por_guiones(fecha_str)
        if len(componentes) != 3:
            return False
        dia_str, mes_str, año_str = componentes
        for s in [dia_str, mes_str, año_str]:
            for c in s:
                if c < '0' or c > '9':
                    return False
                
        dia = int(dia_str)
        mes = int(mes_str)
        año = int(año_str)
        
        hoy = datetime.today()
        if año < hoy.year - 100 or año > hoy.year +5:
            return False
        if 1 <= mes <= 12:
            # Días en cada mes, sin considerar bisiestos
            dias_por_mes = [31, 28, 31, 30, 31, 30,
                            31, 31, 30, 31, 30, 31]
            # Años bisiestos
            if mes == 2:
                if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
                    dias_por_mes[1] = 29
            ultimo_dia = dias_por_mes[mes - 1]
            if 1 <= dia <= ultimo_dia:
                return True
    return False

def es_dni_valido(dni):
    longitud_dni = 0
    for caracter in dni:
        longitud_dni += 1
    if longitud_dni < 7 or longitud_dni > 9:
        return False

    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
    es_string = False
    if type(campo) == str:
        es_string = True
    else:
        return False

    letras_mayusculas = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    letras_minusculas = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

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
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    es_numero = True
    for caracter in str(edad):
        if caracter not in numeros:
            es_numero = False
            break
    if not es_numero:
        return False
    
    edad = int(edad)
    
    if edad < 18 or edad > 100:
        return False
    
    return True