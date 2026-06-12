'''w=[]
word=input("enter the word:")
letter=input("enter the letter to check:")
s=word.split()
w.append(s)
if letter in w:
    print("the letter is not present")
else:
    print("the letter is present")'''

'''l=[1,2,3,4,5,6]
l.remove(6)
print(l)'''

'''l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5,6]
if l1 and l2:
    print("same")
else:
    print("different")'''

#square
'''import turtle
s=turtle.Turtle()
for i in range(4):
    s.forward(100)
    s.right(90)
turtle.done()'''

#reactangle
'''import turtle
s=turtle.Turtle()
for i in range(2):
    s.forward(150)
    s.right(90)
    s.forward(80)
    s.right(90)
turtle.done()'''

#star
'''import turtle
star=turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
    star.right(144)
    star.forward(100)
turtle.done()'''

#triangle
'''import turtle
t=turtle.Turtle()
for i in range(3):
    t.forward(100)
    t.left(120)
turtle.done()'''

#pentagon
'''import turtle
t=turtle.Turtle()
for i in range(5):
    t.forward(100)
    t.right(72)
turtle.done()'''

#red square
'''import turtle
t=turtle.Turtle()
t.color("red")
t.pensize(4)
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()'''

#house with base square and rectangle
'''import turtle
s=turtle.Turtle()
for i in range(4):
    s.forward(100)
    s.right(90)
s.left(45)
s.forward(71)
s.right(90)
s.forward(75)
s.left(45)
s.forward(140)
s.right(90)
s.forward(100)
s.right(90)
s.forward(144)
s.right(90)
s.forward(100)
s.right(90)
s.forward(147)
s.left(90)
s.forward(55)
s.left(90)
s.forward(200)
turtle.done()'''


#house with base rectangle
'''import turtle
s=turtle.Turtle()
for i in range(2):
    s.forward(200)
    s.right(90)
    s.forward(80)
    s.right(90)
s.left(45)
s.forward(80)
s.right(90)
s.forward(81)
s.left(45)
s.forward(89)
s.left(90)
s.forward(61)
s.left(90)
s.forward(150)
turtle.done()'''

#robo face
'''import turtle
t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.pendown()
for i in range(4):
    t.forward(200)
    t.left(90)
t.penup()
t.goto(-60, 20)
t.pendown()
t.circle(20)
t.penup()
t.goto(40, 20)
t.pendown()
t.circle(20)
t.penup()
t.goto(-50, -50)
t.pendown()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
t.penup()
t.goto(-140, 0)
t.pendown()
for i in range(4):
    t.forward(40)
    t.left(90)
t.penup()
t.goto(100, 0)
t.pendown()
for i in range(4):
    t.forward(40)
    t.left(90)
turtle.done()'''

#solar system
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)
mercury = turtle.Turtle()
mercury.shape("circle")
mercury.color("gray")
mercury.shapesize(0.4)
mercury.penup()
venus = turtle.Turtle()
venus.shape("circle")
venus.color("gold")
venus.shapesize(0.7)
venus.penup()
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.shapesize(0.8)
earth.penup()
mars = turtle.Turtle()
mars.shape("circle")
mars.color("red")
mars.shapesize(0.6)
mars.penup()
jupiter = turtle.Turtle()
jupiter.shape("circle")
jupiter.color("orange")
jupiter.shapesize(1.8)
jupiter.penup()
saturn = turtle.Turtle()
saturn.shape("circle")
saturn.color("lightyellow")
saturn.shapesize(1.5)
saturn.penup()
uranus = turtle.Turtle()
uranus.shape("circle")
uranus.color("lightblue")
uranus.shapesize(1.2)
uranus.penup()
neptune = turtle.Turtle()
neptune.shape("circle")
neptune.color("darkblue")
neptune.shapesize(1.1)
neptune.penup()
orbit = turtle.Turtle()
orbit.color("white")
orbit.hideturtle()
orbit.speed(0)
radii = [60, 90, 130, 170, 230, 300, 360, 420]
for r in radii:
    orbit.penup()
    orbit.goto(0, -r)
    orbit.pendown()
    orbit.circle(r)
mercury.goto(0, -60)
mercury.setheading(0)
mercury.circle(60, 45)
venus.goto(0, -90)
venus.setheading(0)
venus.circle(90, 120)
earth.goto(0, -130)
earth.setheading(0)
earth.circle(130, 200)
mars.goto(0, -170)
mars.setheading(0)
mars.circle(170, 30)
jupiter.goto(0, -230)
jupiter.setheading(0)
jupiter.circle(230, 270)
saturn.goto(0, -300)
saturn.setheading(0)
saturn.circle(300, 90)
uranus.goto(0, -360)
uranus.setheading(0)
uranus.circle(360, 160)
neptune.goto(0, -420)
neptune.setheading(0)
neptune.circle(420, 310)
while True:
    mercury.circle(60, 0.8)
    venus.circle(90, 0.6)
    earth.circle(130, 0.4)
    mars.circle(170, 0.3)
    jupiter.circle(230, 0.16)
    saturn.circle(300, 0.12)
    uranus.circle(360, 0.08)
    neptune.circle(420, 0.06)




