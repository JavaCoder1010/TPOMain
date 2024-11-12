import tkinter as tk
from tkinter import ttk

def crear_seleccion_profesiones(ventana, row_position):
    """
    Crea un frame con checkboxes para la selección de profesiones.
    
    Args:
        ventana (tk.Tk): La ventana donde se creará el frame
        row_position (int): La posición de la fila donde se ubicará el frame
        
    Returns:
        tk.StringVar: Variable que contendrá la profesión seleccionada
    """
    # Lista de profesiones
    profesiones = [
        "Comercio/Ventas",
        "Administración/Oficina",
        "Construcción",
        "Educación",
        "Servicios domésticos",
        "Transporte",
        "Salud",
        "Gastronomía",
        "Industria manufacturera",
        "Agricultura y ganadería",
        "Servicios profesionales",
        "Tecnología/Informática",
        "Seguridad",
        "Mantenimiento y reparaciones",
        "Belleza y cuidado personal",
        "Servicios financieros",
        "Logística y distribución",
        "Comunicación y medios",
        "Turismo y hotelería",
        "Entretenimiento y cultura",
        "otro"
    ]
    
    # Crear frame para contener los componentes de profesión
    frame_profesion = ttk.LabelFrame(ventana, text="Seleccione su profesión")
    frame_profesion.grid(row=row_position, column=1, padx=5, pady=5, sticky='w')
    
    # Variable para almacenar la selección
    profesion_var = tk.StringVar()
    profesion_var.set("")  # Valor inicial vacío
    
    # Crear los radiobuttons
    for i, profesion in enumerate(profesiones):
        radio = ttk.Radiobutton(
            frame_profesion,
            text=profesion,
            variable=profesion_var,
            value=profesion
        )
        radio.grid(row=i//2, column=i%2, sticky='w', padx=5, pady=2)
    
    return profesion_var