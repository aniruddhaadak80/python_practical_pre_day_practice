import turtle;
turtle.bgcolor("light blue");
turtle.color("blue");
turtle.shape("circle");
turtle.begin_fill();
for i in range(2):
    turtle.forward(250);
    turtle.left(60);
    turtle.forward(100);
    turtle.left(120);
turtle.end_fill();  
turtle.hideturtle();
turtle.done();  
    