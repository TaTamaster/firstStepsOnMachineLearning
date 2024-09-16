import tkinter as tk
from tkinter import messagebox
import time
import threading

def iniciar_temporizador():
    tiempo_str = entrada.get()
    try:
        h, m, s = map(int, tiempo_str.split(':'))
        tiempo_total = h * 3600 + m * 60 + s
        if tiempo_total <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese el tiempo en formato hh:mm:ss.")
        return

    def cuenta_regresiva(t):
        while t > 0:
            horas, resto = divmod(t, 3600)
            minutos, segundos = divmod(resto, 60)
            formato_tiempo = '{:02d}:{:02d}:{:02d}'.format(horas, minutos, segundos)
            etiqueta.config(text=formato_tiempo)
            time.sleep(1)
            t -= 1
        etiqueta.config(text="00:00:00")
        # Emitir alarma
        for _ in range(5):
            root.bell()
            time.sleep(0.5)

    hilo = threading.Thread(target=cuenta_regresiva, args=(tiempo_total,))
    hilo.start()

root = tk.Tk()
root.title("Temporizador")

entrada = tk.Entry(root, font=("Helvetica", 20))
entrada.pack(pady=10)
entrada.insert(0, "00:00:00")  # Valor predeterminado

boton_iniciar = tk.Button(root, text="Iniciar", command=iniciar_temporizador, font=("Helvetica", 20))
boton_iniciar.pack(pady=10)

etiqueta = tk.Label(root, text="00:00:00", font=("Helvetica", 80))
etiqueta.pack(pady=20)

root.mainloop()