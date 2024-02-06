import turtle;
turtle.bgcolor("pink");
turtle.title("Star using turtle");

turtle.fillcolor("light green");
turtle.begin_fill();

#for loop for creating star in turtle
for i in range(5):
    turtle.forward(200);
    turtle.left(144);

turtle.end_fill();
turtle.hideturtle();   
turtle.done(); 