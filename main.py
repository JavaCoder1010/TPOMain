import frontend
from listas import dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista, bienesArgentinasLista, bienesExterioresLista

def registrar_datos():
    datos = frontend.enviar_datos()
    if datos:
        dniLista.append(datos[0])
        apellidoLista.append(datos[1])
        nombreLista.append(datos[2])
        edadLista.append(datos[3])
        fechaDeNacimientoLista.append(datos[4])
        profesionLista.append(datos[5])
        montoLista.append(datos[6])
        fechaDeclararLista.append(datos[7])
        origenLista.append(datos[8])
        bienesArgentinasLista.append(datos[9])
        bienesExterioresLista.append(datos[10])
    else:
        print("No se registraron datos.")

def main():
    frontend.boton_enviar.config(command=registrar_datos)
    frontend.configurar_boton_mostrar_datos()
    frontend.agregar_boton_salir()
    frontend.ventana.mainloop()

if __name__ == "__main__":
    main()