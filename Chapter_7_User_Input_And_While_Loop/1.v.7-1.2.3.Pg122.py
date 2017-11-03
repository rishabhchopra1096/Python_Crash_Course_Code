#7-1:RENTAL CAR:
'''
car=input("What kind of rental car would you like to buy? ")
vowels=['a','e','i','o','u']
if car[0] not in vowels:
    print ("Let me see if i can find you a "+car.title()+".")
elif car[0] in vowels:
    print ("Let me see if i can find you an "+car.title()+".") '''

#7-2: Restaurant Seating:
'''
people=input("How many people are therr in your dinner group?")
people=int(people)
if people>8:
    print("Sorry, you guys will have to wait for a few minutes.")
elif people<=8:
    print("Your table is ready!")
'''

#7-3:Multiples of Ten:

number=input("give me a number and i will tell you if it is a multiple of 10 or not. ")
number=int(number)
if number%10==0:
    print(str(number)+" is divisible by 10.")
else:
    print (str(number)+" is not divisible by 10.")
