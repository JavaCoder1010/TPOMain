import frontend.interfaz as interfaz
from listas import (
    dniLista,
    apellidoLista,
    nombreLista,
    edadLista,
    fechaDeNacimientoLista,
    profesionLista,
    montoLista,
    fechaDeclararLista,
    origenLista,
    bienesArgentinasLista,
    bienesExterioresLista,
)


def registrar_datos():
    """
    Registra los datos de las entradas y los checkboxes en las listas
    correspondientes.
    """
    datos = interfaz.enviar_datos(
        interfaz.entradas,
        interfaz.variables_bienes_argentina,
        interfaz.variables_bienes_exterior,
    )

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
    """
    Función principal del programa. Inicializa la interfaz gráfica, configura el botón
    de enviar para que llame a la función registrar_datos, y muestra la ventana principal
    en la pantalla.
    """
    ventana, boton_enviar = interfaz.inicializar_interfaz()
    boton_enviar.config(command=registrar_datos)
    ventana.mainloop()


if __name__ == "__main__":
    main()
