import turtle
import time
import random

posponer = 0.05

#Ventana
wn = turtle.Screen()
wn.bgcolor("#F1BEFE")
wn.setup(width = 600, height = 600)

#Serpiente
serp = turtle.Turtle()
serp.speed(0)
serp.shape("square")
serp.color("#59A701")
serp.penup()
serp.goto(0,0)
serp.direction = "stop"

#Comida
manzana = turtle.Turtle()
manzana.shape("circle")
manzana.color("red")
manzana.penup()
manzana.speed(0)
manzana.goto(0,80)

#Segmentos - cuerpo  serpiente
segmentos = []

#Colores comida
color = ["red", "pink", "purple", "orange", "yellow", "blue", "#E85F16", "#DC16E8"]
#Funciones

def mov():

	if serp.direction == "up":
		y = serp.ycor()
		serp.sety(y + 20)

	if serp.direction == "down":
		y = serp.ycor()
		serp.sety(y - 20)

	if serp.direction == "right":
		x = serp.xcor()
		serp.setx(x + 20)

	if serp.direction == "left":
		x = serp.xcor()
		serp.setx(x - 20)

def arriba():
	serp.direction = "up"

def abajo():
	serp.direction = "down"

def derecha():
	serp.direction = "right"

def izquierda():
	serp.direction = "left"

#Teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(derecha, "Right")
wn.onkeypress(izquierda, "Left")

while True:
	wn.update()

	if serp.distance(manzana) < 20:
		x = random.randint(-280,280)
		y = random.randint(-280,280)
		manzana.goto(x,y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.color("#59A701")
		nuevo_segmento.penup()

		segmentos.append(nuevo_segmento)

	totalSeg = len(segmentos)
	
	for index in range(totalSeg -1, 0 , -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)

	if totalSeg > 0:
		x = serp.xcor()	
		y = serp.ycor()
		segmentos[0].goto(x,y)

	mov()
	time.sleep(posponer)

	manzana.color(random.choice(color))
