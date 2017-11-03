number = raw_input("Give me a number and i will tell " +
    "\nyou if it is divisible by 10. ")
number = int(number)

if number%10 == 0:
    print("Yes , " + str(number) + " is divisible by 10.")
else:
    print("No, " + str(number) + " is not divisible by 10.")

