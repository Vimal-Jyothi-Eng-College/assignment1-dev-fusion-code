"""Question: a) Write a Python program to display the given integer in a reverse
manner."""

num=int(input("Enter an Integer: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("Reversed Number is",reverse)