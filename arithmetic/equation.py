# Solve the Quadratic Equation Ax2 + Bx + C=0
a= int (input("enter the value A \n"))
b = int (input ("enter the value B \n"))
c= int (input('enter the of c \n'))
x1=(-b + (b**b-4*a*c)**0.5)/(2*a)
x2=(-b -(b**b-4*a*c)**0.5)/(2*a)
print(x1, x2)
