import frontend
from frontend import enviar_datos


fin = "si"

dniLista = []
apellidoLista = []
nombreLista = []
edadLista = []
fechaDeNacimientoLista = []
profesionLista = []
montoLista = []
fechaDeclararLista = []
origenLista = []

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
        suma += edad
    promedio = (suma/len(edadLista))
    return promedio

def registrardatos():
    dni, apellido, nombre, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen = frontend.enviar_datos
    dniLista.append(dni)
    apellidoLista.append(apellido)
    nombreLista.append(nombre)
    edadLista.append(edad)
    fechaDeNacimientoLista.append(fechaDeNacimiento)
    profesionLista.append(profesion)
    montoLista.append(monto)
    fechaDeclararLista.append(fechaDeclarar)
    origenLista.append(origen)
    return dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista


while fin == "si":
    registrardatos()
    fin = input("¿Quiere realizar otra declaración? (Ingrese 'si' para continuar o 'no' para finalizar): ").lower()

print(f"La edad máxima registrada es {encontrarmax(edadLista)}")
print(f"La edad minima registrada es {encontrarmin(edadLista)}")
print(f"El promedio de edades regsitradas es de {promedioedades(edadLista)}")
cantidad = len(dniLista)
print("La cantidad de personas registradas es", cantidad )

   