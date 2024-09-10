import turtle

# Configuración de la pantalla
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
    pen.circle(60, 60)   # Dibuja un arco de círculo
    pen.left(120)        # Cambia dirección
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

# Ocultar el turtle y finalizar
pen.hideturtle()
screen.mainloop()
