import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox

# Función para dibujar la flor
def draw_flower():
    # Configuración de la pantalla de Turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Crear el objeto turtle
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.speed(10)

    # Función para dibujar un pétalo
    def draw_petal():
        pen.color("red")
        pen.begin_fill()
        pen.circle(60, 60)  # Dibuja un arco de círculo
        pen.left(120)       # Cambia dirección
        pen.circle(60, 60)
        pen.end_fill()
        pen.left(60)

    # Dibujar la flor (6 pétalos)
    for _ in range(6):
        draw_petal()

    # Ajustar posición para el centro de la flor
    pen.penup()
    pen.goto(0, -20)  # Posicionar el turtle justo en el centro
    pen.pendown()

    # Dibujar el centro de la flor
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

    # Ocultar el turtle
    pen.hideturtle()

    # Mantener la ventana Turtle abierta hasta que se cierre
    screen.mainloop()

# Función para mostrar el cuadro de texto después de cerrar Turtle
def show_input_dialog():
    # Crear ventana emergente de texto
    opinion = simpledialog.askstring("Flor", "¿Qué te pareció la flor?")
    
    if opinion:
        # Mostrar un mensaje de agradecimiento
        messagebox.showinfo("Muchas gracias", "¡Muchas gracias por tu opinión!")
    else:
        messagebox.showinfo("Sin opinión", "No has escrito nada.")

# Ejecutar Turtle para dibujar la flor
draw_flower()

# Luego de cerrar la ventana de Turtle, abrir Tkinter para el cuadro de texto
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal de Tkinter

# Mostrar el cuadro de diálogo de texto
show_input_dialog()
