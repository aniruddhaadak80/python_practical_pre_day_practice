fruits = ['Apple', 'Banana', 'cherry', 'mango','mango','oragne', 'orange', 'orange', 'orange'];

# create list -> dictionary  and then dictionary -> list
fruits = list(dict.fromkeys(fruits));

print(fruits);
