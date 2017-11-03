"""The modulo operator: % divides one number by the othe rnumber and returns the remainder.
# it does not tell you how many times one number fits into another , it just tells the remainder.
When a number is divisible by the other number, it has a remanider==0 so it return 0. That is why we can use
this to make a program that tells ypu weather a number is odd or even."""
print (4%3)
print (4%2)

number=input("Enter a number, I'll tell you if it's even or odd.")
# number=int(number)
if number % 2==0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")

# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python even_or_odd_TheModuloOperator.py
# 1
# 0
# Enter a number, I'll tell you if it's even or odd."13"

# The number13is odd.
# When i commented #number=int(number):
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python even_or_odd_TheModuloOperator.py
# 1
# 0
# Enter a number, I'll tell you if it's even or odd."13"
# Traceback (most recent call last):
#   File "even_or_odd_TheModuloOperator.py", line 8, in <module>
#     if number % 2==0:
# TypeError: not all arguments converted during string formatting

# When i uncommented number=int(number):
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python even_or_odd_TheModuloOperator.py
# 1
# 0
# Enter a number, I'll tell you if it's even or odd."13"

# The number 13 is odd.
#Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$
