import tkinter as tk

def mostrar_datos(dniLista, apellidoLista, nombreLista, edadLista, fechaDeNacimientoLista, profesionLista, montoLista, fechaDeclararLista, origenLista, bienes_arg_lista, bienes_ext_lista):
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Ingresados")

    datos_texto = ""
    
    for i in range(len(dniLista)):
        # Datos personales
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
        )

        # Bienes en Argentina
        bienes_nombres_arg = [
            "Moneda", "Inmuebles", "Acciones y participaciones", "Títulos valores",
            "Otros bienes muebles", "Créditos", "Derechos y bienes intangibles",
            "Criptomonedas y criptoactivos", "Otros bienes"
        ]
        
        bienes_encontrados_arg = False
        for j, bien in enumerate(bienes_nombres_arg):
            if bienes_arg_lista[i][j]:
                if not bienes_encontrados_arg:
                    datos_texto += "  Bienes en Argentina:\n"
                    bienes_encontrados_arg = True
                datos_texto += f"    {bien}\n"

        # Bienes en el exterior
        bienes_nombres_ext = [
            "Moneda extranjera", "Inmuebles", "Acciones y participaciones", "Títulos valores",
            "Otros bienes muebles", "Créditos", "Derechos y bienes intangibles", "Otros bienes"
        ]
        
        bienes_encontrados_ext = False
        for k, bien in enumerate(bienes_nombres_ext):
            if bienes_ext_lista[i][k]:  # Solo si es True (Sí)
                if not bienes_encontrados_ext:
                    datos_texto += "  Bienes en el exterior:\n"
                    bienes_encontrados_ext = True
                datos_texto += f"    {bien}\n"

        datos_texto += "-----------------------------------------\n\n"

    # Muestra de datos en una ventana de texto
    text_area = tk.Text(ventana_datos, wrap=tk.WORD, width=80, height=20)
    text_area.insert(tk.END, datos_texto)
    text_area.pack()

    boton_cerrar = tk.Button(ventana_datos, text="Cerrar", command=ventana_datos.destroy)
    boton_cerrar.pack(pady=10)