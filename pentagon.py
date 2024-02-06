import turtle;

turtle.title("Pentagon using turtle ");
turtle.bgcolor("light yellow");

turtle.fillcolor("brown");
turtle.begin_fill();
for i  in range(5):
    turtle.left(72);
    turtle.forward(100);

turtle.end_fill(); 
turtle.hideturtle();
turtle.done();
