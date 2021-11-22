"""
Write a program that asks a user for two integers. Print the smallest integer. If both of the integers are equal, print a statement that the numbers equal.
"""
print("Enter two integers and I will determine which is the smallest one.")
firstInteger = int(input(" Enter the first integer. "))
secondInteger = int(input("Enter the second Integer. "))
if firstInteger == secondInteger:
  print ("They are the same value ")
elif firstInteger > secondInteger:
  print(f"{secondInteger} is the smallest integer")
else:
  print(f"{firstInteger} is the smallest value")
#Compares the integers given