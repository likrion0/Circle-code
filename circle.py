import turtle

def draw_circle(radius):
    turtle.speed(1)  # Velocidad de dibujo (1 = más lento)
    turtle.circle(radius)

# Pide al usuario el radio del círculo
radius = int(input("Ingrese el radio del círculo: "))

# Inicializa la ventana de dibujo
turtle.setup(800, 600)
turtle.title("Dibujar un círculo")
turtle.bgcolor("white")

# Mueve la pluma hacia el centro de la pantalla
turtle.penup()
turtle.goto(0, -radius)
turtle.pendown()

# Dibuja el círculo
draw_circle(radius)

# Cierra la ventana de dibujo al hacer clic en ella
turtle.exitonclick()