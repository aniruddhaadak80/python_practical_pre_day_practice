import turtle;
turtle.bgcolor("light green");

turtle.color("red");

turtle.fillcolor("blue");

turtle.begin_fill();

for i in range(6):
    turtle.forward(100);
    turtle.left(60);

turtle.end_fill();

turtle.hideturtle();

turtle.done();