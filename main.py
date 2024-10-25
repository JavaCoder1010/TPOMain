import frontend
import ver_datos

dniLista = []
apellidoLista = []
nombreLista = []
edadLista = []
fechaDeNacimientoLista = []
profesionLista = []
montoLista = []
fechaDeclararLista = []
origenLista = []

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
       
        # Limpiar el formulario después de registrar los datos
        frontend.limpiar_formulario()

frontend.boton_enviar.config(command=registrardatos)
frontend.configurar_boton_mostrar(ver_datos.mostrar_datos, dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista)
frontend.agregar_boton_salir()

frontend.ventana.mainloop()