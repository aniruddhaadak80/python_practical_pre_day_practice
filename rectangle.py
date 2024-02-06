import turtle;
turtle.shape("turtle");
turtle.title("Rectangle using turtle ");
turtle.bgcolor("light green");
turtle.fillcolor("red");
turtle.begin_fill()
for i in range(2):
    turtle.forward(200);
    turtle.left(90);
    turtle.fd(100);
    turtle.left(90);
turtle.end_fill();
turtle.hideturtle();
turtle.done();