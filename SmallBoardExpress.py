from graphics import  *
import random

def main():

    win = GraphWin('Juego',1400,800, autoflush = False)
    
    #Jugador numero 1
    #Se crea el modelo de la ficha del jugador numero 1.
    #Se dibuja en pantalla y se le pasan valores como los colores, el nombre, tipo de letra, etc.
    p1 = Rectangle(Point(30,30), Point(100,100))
    p1.draw(win)
    p1.move(100,200)
    p1.setFill("red")
    centro1 = p1.getCenter()
    label1 = Text(centro1, "Jugador 1")
    label1.setSize(9)
    label1.setStyle("bold")
    label1.draw(win)

    #Jugador numero 2
    #Se crea el modelo de la ficha del jugador numero 2.
    #Se dibuja en pantalla y se le pasan valores como los colores, el nombre, tipo de letra, etc.
    p2 = Circle(Point(500,250),40)
    p2.draw(win)
    p2.move(-420,15)
    p2.setFill("grey")
    centro2 = p2.getCenter()
    label2 = Text(centro2, "Jugador 2")
    label2.setSize(9)
    label2.setStyle("bold")
    label2.draw(win)
