import math
start=int(input("Enter starting range:"))
end=int(input("Enter end range:"))
for n in range(start,end+1):
 if 100<=n<=9999:
  root=math.isqrt(n)
  if root*root==n and all(int(d)%2==0 for d in str(n)):
    print(n) 
