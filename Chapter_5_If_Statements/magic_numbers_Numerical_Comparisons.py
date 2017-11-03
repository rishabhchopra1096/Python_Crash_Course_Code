answer=17

if answer!=42: #17 is not equal to 42 , so True.
    print "That is not the correct answer. Please try again."
# More comparison operators:
# < means less than and <= means less than equal to
# > means greater than and >= means greater than equal to

age=19
print age<19
print age<=19
print age>=19
print age>19

#Each mathematical comparison can be used as part of an
# if statement, which can help you detect the exact conditions of interest.

print "and & or"
#  You may want to check multiple conditions at the same time. For
# example, sometimes you might need two conditions to be True to take an action.
# Other times you might be satisfied with just one condition being True. The
# keywords and and or can help you in these situations.
print "using and: Passes only if both conditions are true."
age_0=22 #defining age_0
age_1=18 #defining age_1
print age_0>=21 and age_1>=21
#test on the left passes but test on the right fails so the overall answer is False.
age_1 = 22
print age_0 >= 21 and age_1 >= 21
#in this case both conditions are True. Therefore , output is True.

print "\nusing or: Passes when either of the two conditions are met."
age_0=22
age_1=18
print age_0>=21 or age_1>=21
# The left case passes but the right fails , still the output is True as or is used.
age_1 = 22
print age_0 == 21 or age_1 < 21
# Both side fail , so this will output false.


