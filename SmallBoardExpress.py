#SmallBoardExpress
"""SmallBoardExpress
Es un juego de tablero en el que participan dos jugadores lanzando dados.
El jugador que llega primero al último casillero es el que gana."""

from graphics import  *
import random
#Se crea ventana
win = GraphWin('Juego',1400,800, autoflush = False)
#Se inicializa varibale nombre
nombre = ""

#Clase dado
class Dice:
    """Simula un dado de 6 caras."""
    
    def __init__(self,valor):
        """Crea un dado con un determinado valor(valor)"""
        self.valor = valor

    def lanzamiento(self):
        """Simula el lanzamiento del dado. Se obteiene un valor aleatorio
        de acuerdo a las posibles caras del dado."""
        self.valor = random.randint(1,self.valor)

    def getValue(self):
        """Retorna el valor del dado."""
        return self.valor

    def setValue(self,valor):
        """Se pasa valor al dado."""
        self.valor = valor   

#Clase botón
class Button:
    """Simula un botón en la pantalla."""

    def __init__(self,win,p1,p2,label,color1,color2,letra1,letra2,color3,tam):
        """Crea un botón con los parametros correspondientes a dos puntos,
        el nombre del botón, colores, tipos de letras y tamaño."""        
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color1)
        self.rect.setOutline(color2)
        self.rect.draw(win)
        self.label = Text(self.rect.getCenter(),label)
        self.label.setSize(tam)
        self.label.setStyle(letra1)
        self.label.setFace(letra2)
        self.label.setFill(color3)
        self.label.draw(win)

    def setValue(self,label):
        """Se pasa un texto para cambiar el nombre del botón."""
        self.label.setText(label)

#Clase jugador        
class Jugador:
    """Simula la representación de los jugadores en la pantalla."""
    
    def __init__(self,win,forma,p1,p2,c,label,color,tam,letra,a,b):
        """Crea a los jugadores con determinados parámetros como la forma,
        puntos, nombre, color, letra y tamaño."""
        if forma == "rectangulo":
            self.rect = Rectangle(p1,p2)
        else:
            self.rect = Circle(p1,c)
        self.rect.setFill(color)
        self.rect.draw(win)
        self.rect.move(a,b)
        self.label = Text(self.rect.getCenter(),label)
        self.label.setSize(tam)
        self.label.setStyle(letra)
        self.label.draw(win)

    def setMov(self,a,b):
        """Se le pasa valores para el movimiento de los jugadores y el nombre
        que tienen asociados."""
        self.rect.move(a,b)
        self.label.move(a,b)
        self.rect.undraw()
        self.label.undraw()
        self.rect.draw(win)
        self.label.draw(win)
                

#Función correspondiente al movimiento en pantalla del jugador 1
def lanzamientojugador1():
    global nombre
    inicio = 1
    while inicio > 0:
        p = win.getMouse()
        if(50 <= p.getX() <= 200) and (600 <= p.getY() <= 700):
            inicio = 0
    if inicio == 0:
        dadito.setValue(6)
        dadito.lanzamiento()
        dadito.getValue()
        boton2.setValue(dadito.getValue())    
        boton1.setValue("Tirar dado Jugador 2") 
        nombre = "Jugador 2"     
    return (dadito.getValue(),nombre)
    
#Función correspondiente al movimiento en pantalla del jugador 2
def lanzamientojugador2():
    global nombre
    inicio = 1
    while inicio > 0:
        p = win.getMouse()
        if(50 <= p.getX() <= 200) and (600 <= p.getY() <= 700): 
            inicio = 0
    if inicio == 0:
        dadito.setValue(6)
        dadito.lanzamiento()
        dadito.getValue()
        boton2.setValue(dadito.getValue())
        boton1.setValue("Tirar dado Jugador 1")        
        nombre = "Jugador 1"   
    return (dadito.getValue(),nombre)

#Función correspondiente al armado del tablero
def tablero():
    tablero_lineas = [Line(Point(0,180), Point(1500,180)),Line(Point(0,360), Point(1500,360)),
    Line(Point(0,540), Point(1500,540)), Text(Point(120,340),"Inicio de juego"),
    Text(Point(1280,520),"Final del juego")]

    count = 0

    for i in tablero_lineas:
        tl = i
        tl.draw(win)
        count = count + 1
        if (count > 3):
            msj1 = i
            msj1.setStyle("bold")
            msj1.setFace("arial")
            

    rectangulos = [Rectangle(Point(280,180),Point(500,360)),Rectangle(Point(500,180),Point(720,360)),
    Rectangle(Point(720,180),Point(940,360)),Rectangle(Point(940,180),Point(1160,360)),
    Rectangle(Point(280,360),Point(500,540)),Rectangle(Point(500,360),Point(720,540)),
    Rectangle(Point(720,360),Point(940,540)),Rectangle(Point(940,360),Point(1160,540)),
    Rectangle(Point(1160,180),Point(1400,360)),Rectangle(Point(0,360),Point(280,540))]

    colores = ["green","coral","cyan","light blue","orange","gold","light salmon",
    "white","firebrick","lemon chiffon"]
    
    j = 0

    for i in rectangulos:
        a = i
        a.draw(win)
        a.setFill(colores[j])
        j = j + 1
    
    tablero = [Text(Point(380,340),"1"),Text(Point(600,340),"2"),Text(Point(820,340),"3"),
    Text(Point(1040,340),"4"),Text(Point(1280,340),"5"),Text(Point(120,520),"6"),Text(Point(380,520),"7"),
    Text(Point(600,520),"8"),Text(Point(820,520),"9"),Text(Point(1040,520),"10")]

    for i in tablero:
        b = i
        b.setStyle("bold")
        b.draw(win)

dadito = Dice(6)
boton1 = Button(win,Point(50,600),Point(200,700),'Tirar dado Jugador 1',"white","black","bold","arial","black",10)
boton2 = Button(win,Point(350,600),Point(500,700),'',"","","italic","arial","black",12)
boton3 = Button(win,Point(300,600),Point(450,700),'Número :',"","","italic","arial","black",12)
p1 = Jugador(win,"rectangulo",Point(30,30),Point(100,100),0,"Jugador 1","red",9,"bold",100,200)
p2 = Jugador(win,"circulo",Point(500,250),Point(100,100),40,"Jugador 2","grey",9,"bold",-420,15)

def main():

    tablero()
    #Se define la variable pos que representa la posición que ocupa la ficha dentro del tablero.
    pos = 0
    pos2 = 0
        
    while (pos < 11) or (pos2 < 11):
        #Jugador 01
        #Siempre la primera posición va a ser equivalente a cero porque es el punto de partida.
        #Se realiza el "lanzamiento" aleatorio y se avanza a la casilla correspondiente.
        if (pos == 0):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(280,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(500,0)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(720,0)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(940,0)
                pos = pos + 4
            elif (dadito.getValue() == 5):
                p1.setMov(1180,0)
                pos = pos + 5
            elif (dadito.getValue() == 6):
                p1.setMov(0,180)
                pos = pos + 6


        #Posición 1 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 1):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(220,0)
                pos = pos + 1         
            elif (dadito.getValue() == 2):
                p1.setMov(440,0)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(660,0)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(900,0)
                pos = pos + 4
            elif (dadito.getValue() == 5):    
                p1.setMov(-280,180)
                pos = pos + 5
            elif (dadito.getValue() == 6):
                p1.setMov(0,180)
                pos = pos + 6

        #Posición 2 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 2):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(220,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(440,0)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(680,0)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(-500,180)
                pos = pos + 4
            elif (dadito.getValue() == 5):    
                p1.setMov(-220,180)
                pos = pos + 5
            elif (dadito.getValue() == 6):
                p1.setMov(0,180)
                pos = pos + 6        


        #Posición 3 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 3):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(220,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(460,0)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(-720,180)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(-440,180)
                pos = pos + 4
            elif (dadito.getValue() == 5):    
                p1.setMov(-220,180)
                pos = pos + 5
            elif (dadito.getValue() == 6):
                p1.setMov(0,180)
                pos = pos + 6     

        #Posición 4 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 4):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(240,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(-940,180)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(-660,180)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(-440,180)
                pos = pos + 4
            elif (dadito.getValue() == 5):    
                p1.setMov(-220,180)
                pos = pos + 5
            elif (dadito.getValue() == 6):
                p1.setMov(0,180)
                pos = pos + 6                       

        #Posición 5 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 5):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(-1180,180)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(-900,180)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(-680,180)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(-460,180)
                pos = pos + 4
            elif (dadito.getValue() == 5):    
                p1.setMov(-240,180)
                pos = pos + 5
            elif (dadito.getValue() == 6):
                p1.setMov(0,180)
                pos = pos + 6
                break                       

        #Posición 6 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 6):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(280,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(500,0)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(720,0)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(940,0)
                pos = pos + 4
            elif (dadito.getValue() == 5):    
                p1.setMov(1180,0)
                pos = pos + 5
                break
            elif (dadito.getValue() == 6):
                p1.setMov(0,0)
                pos = pos + 0

        #Posición 7 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 7):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(220,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(440,0)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(660,0)
                pos = pos + 3
            elif (dadito.getValue() == 4):
                p1.setMov(900,0)
                pos = pos + 4
                break
            elif (dadito.getValue() == 5):    
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 6):
                p1.setMov(0,0)
                pos = pos + 0                       

        #Posición 8 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 8):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(220,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(440,0)
                pos = pos + 2
            elif (dadito.getValue() == 3):
                p1.setMov(680,0)
                pos = pos + 3
                break
            elif (dadito.getValue() == 4):
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 5):    
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 6):
                p1.setMov(0,0)
                pos = pos + 0  

        #Posición 9 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 9):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(220,0)
                pos = pos + 1
            elif (dadito.getValue() == 2):
                p1.setMov(460,0)
                pos = pos + 2
                break
            elif (dadito.getValue() == 3):
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 4):
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 5):    
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 6):
                p1.setMov(0,0)
                pos = pos + 0  

        #Posición 10 - para el Jugador 01
        if (nombre == "Jugador 1") and (pos == 10):
            lanzamientojugador1()
            if (dadito.getValue() == 1):
                p1.setMov(240,0)
                pos = pos + 1
                break
            elif (dadito.getValue() == 2):
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 3):
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 4):
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 5):    
                p1.setMov(0,0)
                pos = pos + 0
            elif (dadito.getValue() == 6):
                p1.setMov(0,0)
                pos = pos + 0


        #Jugador02
        if (nombre == "Jugador 2") and (pos2 == 0):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(250,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(470,0)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(690,0)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(910,0)
                pos2 = pos2 + 4
            elif (dadito.getValue() == 5):
                p2.setMov(1130,0)
                pos2 = pos2 + 5
            elif (dadito.getValue() == 6):
                p2.setMov(0,180)
                pos2 = pos2 + 6
        
        #Posición 01 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 1):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(440,0)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(660,0)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(880,0)
                pos2 = pos2 + 4
            elif (dadito.getValue() == 5):    
                p2.setMov(-250,180)
                pos2 = pos2 + 5
                p2.undraw()
            elif (dadito.getValue() == 6):
                p2.setMov(0,180)
                pos2 = pos2 + 6

        #Posición 02 - para el Jugador 02        
        if (nombre == "Jugador 2") and (pos2 == 2):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(440,0)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(660,0)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(-470,180)
                pos2 = pos2 + 4
            elif (dadito.getValue() == 5):    
                p2.setMov(-220,180)
                pos2 = pos2 + 5
            elif (dadito.getValue() == 6):
                p2.setMov(0,180)
                pos2 = pos2 + 6                
        
        #Posición 03 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 3):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(440,0)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(-690,180)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(-440,180)
                pos2 = pos2 + 4
            elif (dadito.getValue() == 5):    
                p2.setMov(-220,180)
                pos2 = pos2 + 5
            elif (dadito.getValue() == 6):
                p2.setMov(0,180)
                pos2 = pos2 + 6        
        
        #Posición 04 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 4):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(-910,180)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(-660,180)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(-440,180)
                pos2 = pos2 + 4
            elif (dadito.getValue() == 5):    
                p2.setMov(-220,180)
                pos2 = pos2 + 5
            elif (dadito.getValue() == 6):
                p2.setMov(0,180)
                pos2 = pos2 + 6        
        
        #Posición 05 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 5):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(-1130,180)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(-880,180)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(-660,180)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(-440,180)
                pos2 = pos2 + 4
            elif (dadito.getValue() == 5):    
                p2.setMov(-220,180)
                pos2 = pos2 + 5
            elif (dadito.getValue() == 6):
                p2.setMov(0,180)
                pos2 = pos2 + 6
                break                       
        
        #Posición 06 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 6):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(250,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(470,0)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(690,0)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(910,0)
                pos2 = pos2 + 4
            elif (dadito.getValue() == 5):    
                p2.setMov(1130,0)
                pos2 = pos2 + 5
                break
            elif (dadito.getValue() == 6):
                p2.setMov(0,0)
                pos2 = pos2 + 0 

        #Posición 07 - para el Jugador 02                                              
        if (nombre == "Jugador 2") and  (pos2 == 7):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(440,0)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(660,0)
                pos2 = pos2 + 3
            elif (dadito.getValue() == 4):
                p2.setMov(900,0)
                pos2 = pos2 + 4
                break
            elif (dadito.getValue() == 5):    
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 6):
                p2.setMov(0,0)
                pos2 = pos2 + 0                       
        
        #Posición 08 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 8):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(440,0)
                pos2 = pos2 + 2
            elif (dadito.getValue() == 3):
                p2.setMov(680,0)
                pos2 = pos2 + 3
                break
            elif (dadito.getValue() == 4):
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 5):    
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 6):
                p2.setMov(0,0)
                pos2 = pos2 + 0  

        #Posición 09 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 9):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
            elif (dadito.getValue() == 2):
                p2.setMov(440,0)
                pos2 = pos2 + 2
                break
            elif (dadito.getValue() == 3):
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 4):
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 5):    
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 6):
                p2.setMov(0,0)
                pos2 = pos2 + 0  
        
        #Posición 10 - para el Jugador 02
        if (nombre == "Jugador 2") and (pos2 == 10):
            lanzamientojugador2()
            if (dadito.getValue() == 1):
                p2.setMov(220,0)
                pos2 = pos2 + 1
                break
            elif (dadito.getValue() == 2):
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 3):
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 4):
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 5):    
                p2.setMov(0,0)
                pos2 = pos2 + 0
            elif (dadito.getValue() == 6):
                p2.setMov(0,0)
                pos2 = pos2 + 0

        update(50)
    
    #Se muestra en la ventana un mensaje con el jugador que gano la partida
    if (pos == 11):
        mensajefinal = Text(Point(1000,650),"Ganador : Jugador 1")
        mensajefinal.draw(win)
        mensajefinal.setStyle("bold")
    elif (pos2 == 11):
        mensajefinal = Text(Point(1000,650),"Ganador : Jugador 2")    
        mensajefinal.draw(win)
        mensajefinal.setStyle("bold")
    
    #Se espera que se realice un click para finalizar/cerrar la ventana
    mensajecerrar = Text(Point(700,700),"Haga un click para cerrar la ventana")
    mensajecerrar.draw(win)
    mensajecerrar.setSize(15)
    win.getMouse()
    win.close()

main()