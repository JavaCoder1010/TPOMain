import frontend

dniLista = []
apellidoLista = []
nombreLista = []
edadLista = []
fechaDeNacimientoLista = []
profesionLista = []
montoLista = []
fechaDeclararLista = []
origenLista = []

# Nueva función que registra los datos
def registrardatos():
    datos = frontend.enviar_datos()
    if datos:  # Si se retornan datos válidos (es decir, no hubo error)
        dni, apellido, nombre, edad, fechaDeNacimiento, profesion, monto, fechaDeclarar, origen = datos
        dniLista.append(dni)
        apellidoLista.append(apellido)
        nombreLista.append(nombre)
        edadLista.append(edad)
        fechaDeNacimientoLista.append(fechaDeNacimiento)
        profesionLista.append(profesion)
        montoLista.append(monto)
        fechaDeclararLista.append(fechaDeclarar)
        origenLista.append(origen)

# Muestra estadísticas al finalizar la aplicación
def mostrar_estadisticas():
    if edadLista:
        print(f"La edad máxima registrada es {max(edadLista)}")
        print(f"La edad minima registrada es {min(edadLista)}")
        print(f"El promedio de edades registradas es de {sum(edadLista) / len(edadLista)}")
        print(f"La cantidad de personas registradas es {len(dniLista)}")
    else:
        print("No se ha registrado ninguna edad.")

frontend.ventana.protocol("WM_DELETE_WINDOW", lambda: [mostrar_estadisticas(), frontend.ventana.destroy()])
frontend.ventana.mainloop()
