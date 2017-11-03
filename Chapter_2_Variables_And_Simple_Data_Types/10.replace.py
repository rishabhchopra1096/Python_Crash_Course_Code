# str.replace(old, new[, max])
# Parameters:
# old – This is the old substring to be replaced.
# new : The is the new substring which would replace the old substring.
# max : If this optional argument max is given , only the first count occurences are replaced.
# max here refers to the number of replacements you want to make.


line = "hello, my name is hello but you can call me hello"
print("Replacing all 'hello':")
print(line.replace('hello','hey'))

print("\nReplacing 1st instance only. ")
print(line.replace('hello','hey',1))


