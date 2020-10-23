import turtle as trtl
t = trtl.Turtle()

#Draw Shrubbury Details

t.penup()
t.goto(-50,50)
t.pendown()
t.pensize(7)

def small_bush():
  for i in range(5):
    t.color("lime")
    t.begin_fill()
    t.circle(2.5)
    t.end_fill()
    t.right(50)
    

small_bush()

def medium_bush():
  for i in range(6):
    t.pensize(7)
    t.begin_fill()
    t.color("green")
    t.circle(4)
    t.end_fill()
    t.right(40)
    t.forward(5)

t.penup()
t.goto(50,50)
t.pendown()
t.pensize(7)

medium_bush()

t.right(50)
t.forward(10)
t.right(130)
t.pensize(9)
t.forward(10)

def main_bush():
    t.color("forest green")
    t.circle(4)
    t.left(90)
    t.forward(8)
    t.right(90)
    t.circle(4/2)
    t.left(90)
    t.forward(8)
    t.right(90)
    t.circle(4/4)
    t.left(90)
    t.forward(8)
    t.right(90)

t.penup()
t.goto(-50,-50)
t.right(45)
t.pendown()
main_bush()

def small_grass():
  t.pensize(3)
  t.color("olive drab")
  t.left(90)
  t.circle(4,90)
  t.penup()
  t.circle(4,270)
  t.pendown()
  t.forward(4)
  t.backward(4)
  t.right(180)
  t.penup()
  t.circle(4,270)
  t.pendown()
  t.circle(4,90)

t.penup()
t.goto(50,-50)
t.pendown()
small_grass()
t.penup()
t.goto(0,0)

wn = trtl.Screen()
wn.mainloop()


