import tkinter as tk

def mostrar_datos(dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista):
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Ingresados")

    datos_texto = ""
    for i in range(len(dniLista)):
        datos_texto += (
            f"Registro {i+1}:\n"
            f"  DNI                : {dniLista[i]}\n"
            f"  Apellido           : {apellidoLista[i]}\n"
            f"  Nombre             : {nombreLista[i]}\n"
            f"  Edad               : {edadLista[i]}\n"
            f"  Fecha de Nacimiento: {fechaDeNacimientoLista[i]}\n"
            f"  Profesión          : {profesionLista[i]}\n"
            f"  Monto              : {montoLista[i]}\n"
            f"  Fecha Declarar     : {fechaDeclararLista[i]}\n"
            f"  Origen             : {origenLista[i]}\n"
            "-----------------------------------------\n\n"
        )

    text_area = tk.Text(ventana_datos, wrap=tk.WORD, width=80, height=20)
    text_area.insert(tk.END, datos_texto)
    text_area.pack()

    boton_cerrar = tk.Button(ventana_datos, text="Cerrar", command=ventana_datos.destroy)
    boton_cerrar.pack(pady=10)