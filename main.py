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
        
        # Limpiar el formulario
        frontend.limpiar_formulario()



# Asignar la función al botón "Enviar"
frontend.boton_enviar.config(command=registrardatos)
frontend.ventana.mainloop()
