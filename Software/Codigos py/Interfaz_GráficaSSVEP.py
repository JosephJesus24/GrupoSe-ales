import tkinter as tk
import pylsl

# Configuración de la interfaz de LSL
stream_name = "SSVEP_Keyboard"
channel_count = 1  # Número de canales EEG utilizados
sampling_rate = 250  # Tasa de muestreo en Hz

# Configuración del teclado virtual
keyboard_layout = [
    {'letra': 'A', 'frecuencia': 6.67},
    {'letra': 'B', 'frecuencia': 10.0},
    {'letra': 'C', 'frecuencia': 5.88},
    {'letra': 'D', 'frecuencia': 7.57}
]

# Colores
background_color = 'black'
button_text_color = 'white'

# Crear una ventana
window = tk.Tk()
window.configure(bg=background_color)

# Obtener el tamaño de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

def on_key_press(event):
    """
    Función que se ejecuta cuando se presiona una tecla del teclado virtual.
    Puedes agregar aquí la lógica que desees realizar al seleccionar una letra.
    """
    letra_seleccionada = event.widget["text"]
    print("Letra seleccionada:", letra_seleccionada)

def toggle_button_color(button, color1, color2):
    """
    Función que alterna el color de fondo del botón entre color1 y color2.
    """
    current_color = button["bg"]
    next_color = color2 if current_color == color1 else color1
    button.configure(bg=next_color)
    window.after(int(1000 / button_data['frecuencia']), toggle_button_color, button, color1, color2)

# Crear los botones del teclado virtual
for i, button_data in enumerate(keyboard_layout):
    letra = button_data['letra']
    
    button = tk.Button(window, text=letra, width=33, height=15, fg=button_text_color)
    
    # Establecer las coordenadas para ubicar los botones en las esquinas
    if i == 0:  # Esquina superior izquierda
        button.grid(row=0, column=0, padx=15, pady=10)
    elif i == 1:  # Esquina superior derecha
        button.grid(row=0, column=1, padx=1000, pady=10)
    elif i == 2:  # Esquina inferior izquierda
        button.grid(row=1, column=0, padx=15, pady=280)
    elif i == 3:  # Esquina inferior derecha
        button.grid(row=1, column=1, padx=15, pady=280)
    
    button.bind("<Button-1>", on_key_press)
    
    # Configurar el parpadeo de la frecuencia utilizando una animación
    color1 = background_color
    color2 = 'green2'
    window.after(int(1000 / button_data['frecuencia']), toggle_button_color, button, color1, color2)

# Bucle principal de la ventana
window.mainloop()
