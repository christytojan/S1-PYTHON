import arithmetic.calculator

print("1.Adition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

ch=int(input("Enter you choice:"))
if ch==1:
  arithmetic.calculator.addition()
  
elif ch==2:
  arithmetic.calculator.subtraction()  
  
elif ch==3:
  arithmetic.calculator.multiplication()
  
elif ch==4:
  arithmetic.calculator.division()  
  
else:
  print("Invalid choice")  
