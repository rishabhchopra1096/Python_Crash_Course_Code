#age=23
#message="Happy "+age+"rd Birthday"
#print (message)
#TypeError: cannot concatenate 'str' and 'int' objects.
#[Finished in 1.1s with exit code 1]
#[shell_cmd: python -u "/Users/rishabhchopra/Downloads/python_work/birthday.py"]
#[dir: /Users/rishabhchopra/Downloads/python_work]
#[path: /usr/bin:/bin:/usr/sbin:/sbin]
#--> Python knows that the variable could represent either the numerical value 23
# or the characters 2 and 3. When you use integers within strings like this,
# you need to specify explicitly that you want Python to use the integer as a string
# of characters. You can do this by wrapping the variable in the str() function, which
# tells Python to represent non-string values as strings:
age = 23
message = "Happy " + str(age) + "rd Birthday"
print (message)
#or
age="23"
message="Happy "+ age + "rd Birthday"
print (message) #will print the same result

# #now,for:
# x=hello
# print x #NameError: name 'hello' is not defined
# #lesson2: python does not accept plain text as a value to a variable or just genrally also.
# #lesson1:strings can be added to strings or variables whose value is a string ONLY
# #lesson1: sum_of_strings="string"+(variable="string")/"string"
# import this
