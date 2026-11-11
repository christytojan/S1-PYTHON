import graphics.rectangle
from graphics import circle
from graphics.graphics3d import cuboid
from graphics.graphics3d.sphere import sphere

def display(n):
 if n==1:
   graphics.rectangle.rectangle()
 elif n==2:
   circle.circle()
 elif n==3:
   cuboid.cuboid()
 elif n==4:
   sphere()
 elif n==5:
    print("Program ended")
    return
 else:
   print("Invalid choice")
   
 display(int(input("\nEnter Choice(1-5):")))
 
print("1.Rectangle")           
print("2.Circle")           
print("3.Cuboid")           
print("4.Sphere")
print("5.Exit")           
         
display(int(input("Enter choice(1-5):")))         
         

