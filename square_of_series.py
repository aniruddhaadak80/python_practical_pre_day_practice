n = int(input("Enter the value of n : "));

sum =0;
for i in range(1,n+1):
    sum = sum + i*i;
print(f"Sum of the series 1^2 + 2^2 +3^2 +...+{n}^2 : {sum}. ");
