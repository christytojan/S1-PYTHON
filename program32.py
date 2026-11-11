lim=int(input("Enter the limit:"))
for row in range(1,lim+1):
  for space in range(lim-row):
    print(" ",end=" ")
  for colm in range(2*row-1):
    print("*",end=" ")
  print()   
