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
    dni = (input("Ingrese su DNI: "))
    dniLista.append(dni)
    apellido = input("Ingrese su apellido: ")
    apellidoLista.append(apellido)
    nombre = input("Ingrese su nombre: ")
    nombreLista.append(nombre)
    edad = (int(input("Ingrese su edad: ")))
    edadLista.append(edad)
    fechaDeNacimiento = input("Ingrese su fecha de nacimiento (DD/MM/YY): ")
    fechaDeNacimientoLista.append(fechaDeNacimiento)
    profesion = input("Indique su profesión: ")
    profesionLista.append(profesion)
    monto = int(input("Indique el monto a declarar (en dolares): $"))
    montoLista.append(monto)
    fechaDeclarar = input("Indique la fecha en la cual está declarando sus fondos (DD/MM/YY): ")
    fechaDeclararLista.append(fechaDeclarar)
    origen = input("Indique el origen de sus fondos: ")
    origenLista.append(origen)
    return edadLista


while fin == "si":
    registrardatos()
    fin = input("¿Quiere realizar otra declaración? (Ingrese 'si' para continuar o 'no' para finalizar): ").lower()

print(f"La edad máxima registrada es {encontrarmax(edadLista)}")
print(f"La edad minima registrada es {encontrarmin(edadLista)}")
print(f"El promedio de edades regsitradas es de {promedioedades(edadLista)}")
cantidad = len(dniLista)
print("La cantidad de personas registradas es", cantidad )

   