"""
                    Homework-1
*Take 5 values from the user and write a program that prints the calues you get on the screen.

*Print the type of values received in this program on the screen.

*When using print functions, do not forget to use f-string and format usage in your program.

"""

x = input("First value: ")
y = int(input("Second value(int): "))
z = float(input("Third value(float): "))
t = input("4th value: ")
k = int(input("5th value(int): "))

print(f"1st value:{x} and its' type:{type(x)}\n2nd value:{y} and its' type:{type(y)}\n3rd value:{z} and its' type:{type(z)}\n4th value:{t} and its' type:{type(t)}\n5th value:{k} and its' type:{type(k)}")