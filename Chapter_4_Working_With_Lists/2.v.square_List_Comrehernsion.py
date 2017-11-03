#The approach described earlier for generating the list squares consisted of using three or four lines of code.
#A list comprehension allows you to generate this same list in just one line of code.
#A list comprehension combines the for loop
#and the creation of new elements
#into one line, and automatically appends each new element.

squares=[value**2 for value in range(1,11)]# [so what this line is saying is that
#Square each value(value**2) for each value in range(1,11) and put in in a list,hence, the square brackets.]
print squares
#The for loop in this example is for value in range(1,11), which feeds the values 1 through 10 into the expression value**2.
#Lesson:Format for List Comprehension: [expression_with_value for value in .......(it could be a string, a list , a range, any data structure) ]
#Note: no print is used in list comprehensions.
# Notice that no colon is used at the end of the for statement.

#FORMAT FOR LIST COMPRESHENSION:
#comprehended_list=[what_you_want_to_do_with_the_variable for variable in list_name]
#for eg:
list_name=['variable1','variable2','variable3']
comprehended_list=["This is "+variable for variable in list_name]
print comprehended_list