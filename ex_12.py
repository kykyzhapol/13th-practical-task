#12th
import turtle as t
import math as m


def square(x, y, l, angle, color): #x,y - coordinates, l - length
    t.up()
    t.pen(pencolor='white', fillcolor=color, pensize=1) #settings of pen
    t.setposition(x, y)
    t.down()
    t.begin_fill()
    t.left(angle) #value for rotating (like trigonometric circle)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90 + angle) #rotating back for another figures
    t.end_fill()
    t.up()


def triangle(x, y, l, angle, color): #x,y - coordinates, l - length
    t.pen(pencolor='white', fillcolor=color, pensize=1) #settings of pen
    t.setposition(x, y)
    t.begin_fill()
    t.left(angle) #value for rotating (like trigonometric circle)
    t.right(45)
    t.forward(l)
    t.right(135)
    t.forward(l * m.sqrt(2))
    t.right(135)
    t.forward(l)
    t.right(45 + angle) #rotating back for another figures
    t.end_fill()
    t.up()


def parallelogram(x, y, l, angle, color): #x,y - coordinates, l - length
    t.up()
    t.pen(pencolor='white', fillcolor=color, pensize=1)
    t.setposition(x, y)
    t.down()
    t.begin_fill()
    t.left(angle) #value for rotating (like trigonometric circle)
    t.forward(l*m.sqrt(2))
    t.right(135)
    t.forward(l)
    t.right(45)
    t.forward(l*m.sqrt(2))
    t.right(135)
    t.forward(l)
    t.right(45+angle) #rotating back for another figures
    t.up()
    t.end_fill()


def main():
    parallelogram(0,0, 125, 0, 'black')
    square(0,0, 150, 165, 'orange')
    triangle(20, 0, 100, 135, 'red')
    t.mainloop()


if __name__ == '__main__':
    main()