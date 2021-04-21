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

        #Tablero
    #Se disena el tablero con tres lineas paralelas, formando un camino.
    linea1 = Line(Point(0,180), Point(1500,180))
    linea1.draw(win)
    linea2 = Line(Point(0,360), Point(1500,360))
    linea2.draw(win)
    linea3 = Line(Point(0,540), Point(1500,540))
    linea3.draw(win)
    mensaje1 = Text(Point(120,340),"Inicio de juego")
    mensaje1.setStyle("bold")
    mensaje1.setFace("arial")
    mensaje1.draw(win)
    
    #Tablero - lineas
    #Se realizan rectangulos para demilitar los casilleros, los cuales seran 11.
    l1 = Rectangle(Point(280,180),Point(500,360))
    l1.draw(win)
    l1.setFill("green")
    
    l2 = Rectangle(Point(500,180),Point(720,360))
    l2.draw(win)
    l2.setFill("coral")
    
    l3 = Rectangle(Point(720,180),Point(940,360))
    l3.draw(win)
    l3.setFill("cyan")
    
    l4 = Rectangle(Point(940,180),Point(1160,360))
    l4.draw(win)
    l4.setFill("light blue")
    
    l5 = Rectangle(Point(280,360),Point(500,540))
    l5.draw(win)
    l5.setFill("orange")

    l6 = Rectangle(Point(500,360),Point(720,540))
    l6.draw(win)
    l6.setFill("gold")
    
    l7 = Rectangle(Point(720,360),Point(940,540))
    l7.draw(win)
    l7.setFill("light salmon")
    
    l8 = Rectangle(Point(940,360),Point(1160,540))
    l8.draw(win)
    l8.setFill("white")

    l9 = Rectangle(Point(1160,180),Point(1400,360))
    l9.draw(win)
    l9.setFill("firebrick")

    l10 = Rectangle(Point(0,360),Point(280,540))
    l10.draw(win)
    l10.setFill("lemon chiffon")

    labeltablero1 = Text(Point(380,340),"1")
    labeltablero1.setStyle("bold")
    labeltablero1.draw(win)
    labeltablero2 = Text(Point(600,340),"2")
    labeltablero2.setStyle("bold")
    labeltablero2.draw(win)
    labeltablero3 = Text(Point(820,340),"3")
    labeltablero3.setStyle("bold")
    labeltablero3.draw(win)
    labeltablero4 = Text(Point(1040,340),"4")
    labeltablero4.setStyle("bold")
    labeltablero4.draw(win)
    labeltablero5 = Text(Point(1280,340),"5")
    labeltablero5.setStyle("bold")
    labeltablero5.draw(win)
    labeltablero6 = Text(Point(120,520),"6")
    labeltablero6.setStyle("bold")
    labeltablero6.draw(win)
    labeltablero7 = Text(Point(380,520),"7")
    labeltablero7.setStyle("bold")
    labeltablero7.draw(win)
    labeltablero8 = Text(Point(600,520),"8")
    labeltablero8.setStyle("bold")
    labeltablero8.draw(win)
    labeltablero8 = Text(Point(820,520),"9")
    labeltablero8.setStyle("bold")
    labeltablero8.draw(win)
    labeltablero8 = Text(Point(1040,520),"10")
    labeltablero8.setStyle("bold")
    labeltablero8.draw(win)

    
    mensaje2 = Text(Point(1280,520),"Final del juego")
    mensaje2.setStyle("bold")
    mensaje2.setFace("arial")
    mensaje2.draw(win)

    #Dado
    #Se crea el "dado" y se configura el texto del boton que tendra la funcion de "arrojar" el dado.   
    dado = Rectangle(Point(50,600), Point(200,700)).draw(win)
    boton = Text(dado.getCenter(),"Tirar dado Jugador 1")
    boton.setSize(10)
    boton.setStyle("bold")
    boton.setFace("arial")
    dado.setFill("white")
    boton.draw(win)
    cara = Text(Point(350,650),"Número :")
    cara.setStyle("italic")
    cara.draw(win)
    salida = Text(Point(400,650),"")
    salida.setStyle("italic")
    salida.draw(win)

