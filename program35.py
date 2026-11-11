square=lambda s:s*s
rectangle=lambda l,b:l*b
triangle= lambda bs,h:0.5*bs*h
s=float(input("Enter side of the square:"))
l=float(input("Enter length of the rectangle:"))
b=float(input("Enter breadth of the rectangle:"))
bs=float(input("Enter base of the triangle:"))
h=float(input("Enter height of the triangle:"))

print("Area of square=",square(s))
print("Area of rectangle=",rectangle(l,b))
print("Area of triangle=",triangle(bs,h))

