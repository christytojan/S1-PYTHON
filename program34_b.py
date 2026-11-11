vote= lambda age:"Eligible to vote" if age>=18 else "not eligible to vote"
age=int(input("Enter your age"))
print(vote(age))
