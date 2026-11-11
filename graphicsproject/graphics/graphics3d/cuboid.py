def cuboid():
  l=float(input("Enter length:"))
  b=float(input("Enter breadth:"))
  h=float(input("Enter height:"))
  area=2*(l*b+b*h+h*l)
  perimeter=4*(l+b+h)
  print("Surface area of cuboid=",area)
  print("Total Edge Length of Cuboid=",perimeter)
