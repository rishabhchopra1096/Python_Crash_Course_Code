d# print "Writing Clear Prompts"
# name =input("Please enter your name: ")
# print ("Hello, "+name+"!")
#TERMINAL :
# Rishabhs-MacBook-Pro:~ rishabhchopra$ cd Desktop/IPND/python_work
# Rishabhs-MacBook-Pro:python_work rishabhchopra$ ls
# Chapter_2_Variables_And_Simple_Data_Types
# Chapter_3_Intoducing_Lists
# Chapter_4_Working_With_Lists
# Chapter_5_If_Statements
# Chapter_6_Dictionaries
# Chapter_7_User_Input_And_While_Loop
# Python Crash Course.pdf
# Rishabhs-MacBook-Pro:python_work rishabhchopra$ cd Chapter_7_User_Input_And_While_Loop
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ ls
# greeter_Writing_Clear_Prompts.py    parrot_How_the_input_function_works.py
# parrotForTerminal.py
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ cd greeter_Writing_Clear_Prompts.py
# -bash: cd: greeter_Writing_Clear_Prompts.py: Not a directory
""" Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python greeter_Writing_Clear_Prompts.py
 Writing Clear Prompts
# Please enter your name: "Rishabh"
# Hello, Rishabh! """
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$

#Sometimes , you will want to write a prompt thats longer than one line.
# For example, you might want to tell the user why youre asking for certain input.
# For this ,save your prompt in a variable and pass that variable to the input() funtion.
# This allows you to build your prompt over several lines, then wite a clean input() statement.

prompt="If you tell us who you are , we can personalize the messages you see."
prompt= prompt+"\nWhat is your name? "# Do not forget to use the space mark after the question.
name = input(prompt)
print ("\nHello, "+name+"!")
# TERMINAL:
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$ python greeter_Writing_Clear_Prompts.py
# If you tell us who you are , we can personalize the messages you see.
# What is your name? "Rishabh"

# Hello, Rishabh!
# Rishabhs-MacBook-Pro:Chapter_7_User_Input_And_While_Loop rishabhchopra$

"""Lesson:
1. format for using input function:
variable=input(prompt)
The prompt should have a space at the end of it to make it clear to the user where to enter the text.
The prompt can be any sentence , can be distributed over lines, with whitespaces betyween it.
The input function just does half of the work.
Once the input function recieve the input from the user, that input is stored in the variable and it can be used later in the
program.
Mostly, an input statement just contains a direct question to the user.
Part of writing prompts clearly is distributing them on different lines, telling the user why they need to enter
that input."""




