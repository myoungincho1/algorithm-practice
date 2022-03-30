#Assignment 1
print('%0.4f'%4.12341234) #'4.1234'
print('%12.4f'%4.12341234) #'      4.1234'

#Assignment 2
import turtle
turtle.setup(width=1000, height=600)
t = turtle.Turtle()
t.shape('turtle')
t.forward(100)
s = turtle.textinput('','enter your name:')
t.write('Hello? %s This is Turtle'% s)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)