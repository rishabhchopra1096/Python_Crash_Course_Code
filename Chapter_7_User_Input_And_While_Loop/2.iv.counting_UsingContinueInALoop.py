#Using continue in a Loop
#Rather than breaking out of a loop entirely without executing the rest of its code,
# you can use the continue statement to return to the beginning of the loop based on
#the result of a conditional test. For example, consider a loop that counts from 1 to 10
#but prints only the odd numbers in that range.

current_number=0
while current_number<10:
    current_number+=1
    if current_number % 2==0:
        continue
    print (current_number)

# 1. First we set current_number to 0. Because its less than 10, Python enters the while loop.
# 2. Once inside the loop, we increment the count by 1 , so current_number is 1.
# 3. The if statement then checks the modulo of current_number and 2.
'''i) If the modulo is 0 (which means current_number is divisible by 2), the continue statement tells Python to ignore the
rest of the loop and return to the beginning.'''
#   ii) If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number.
# Simple, so starting with 0:
# then cn = 1 --> Not divisible by 2 , gets printed. And while loop starts again.
# Now cn = 2 --> Divisible by 2 , continue statement ignores the loop and starts again.
# Now cn= 2+1=3 --> Not divisible by 2 , gets printed. And while loop starts again.
# and this goes on..
# This is how you miss the even numbers.
'''The difference between continue and break is that,
break: stops the execution of further lines of code.
continue: stops the excution and brings back the line of code to the starting of loop.
'''


x=['Hello',"hello",'No',"WHAT",'hello']
x=x.replace('hello','no')
print(x)