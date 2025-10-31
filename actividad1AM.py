"""Paint, for drawing shapes
EQUIPO ANDY Y GAEL
"""

from turtle import *

from freegames import vector
import math

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

"""
up levanta el pincel
go to mueve a la tortuga
down pinta
"""




def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()








"""--------------------NUESTROS CAMBIOS FUERON: GAEL WASO-----------------"""

def Circle(start, end):
    """Dibuja un círculo desde start hasta end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    """OBTIENE EL RADIO MEDIANTE LA DISTANCIA ENTRE START Y END"""
    radio = ((end.x - start.x)**2 + (end.y - start.y)**2) ** 0.5

    """SE MUEVE HACIA EL MEDIO, Y POSTERIORMENTE HACIA ABAJO, PARA EMPEZAR A IMPRIMIR EL CIRCULO"""
    up()
    goto(start.x, start.y - radio)
    down()

    """DIBUJA EL CIRCULO MEDIANTE LA FUNCION TURTLE_CIRCLE"""
    circle(radio)

    end_fill()



"""---------------FIN DE CAMBIOS REALIZADOS, GAEL WASO----------------"""


"""

INICIO CAMBIOS ANDY
VAMOS A HACER EL RECTANGULO Y EL TRIANGULO

"""


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    """ mover tortuga al punto inicial"""
    down()
    begin_fill()
    """ empieza a rellenar color"""

    width = end.x - start.x
    height = end.y - start.y

    forward(width)
    """ lado superior"""
    left(90)
    forward(height)         
    """ lado derecho"""
    left(90)
    forward(width)          
    """ lado inferior """
    left(90)
    forward(height)        
    """ lado izquierdo"""
    left(90)

    end_fill()              
    """ termina de rellenar"""


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)  # ir al punto inicial
    down()
    begin_fill()             # empezar a rellenar

    # Calculamos los 3 puntos del triángulo
    x0, y0 = start.x, start.y
    x1, y1 = end.x, end.y

    # Primer lado: de start a end
    goto(x1, y1)

    # Segundo lado: triangular (base horizontal)
    goto(x0, y1)

    # Tercer lado: cerrar triángulo
    goto(x0, y0)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')



"""------------CAMBIOS REALIZADOS: GAEL WASO-------------"""

onkey(lambda: color('pink'), 'P')

"""------------FIN DE CAMBIOS REALIZADOS GAEL WASO-------------"""



onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', Circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
