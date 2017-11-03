first_name="ada"
last_name="lovelace"

full_name=first_name+" "+last_name
print (full_name)

print (full_name.title()) #thought .title() can be applied to strings only?
                        # worked cause full_name is a string that is a concatenation of strings#
message = "Hello, "+ full_name + "!"
print (message)
print (message.title())
#or#
message="Hello, " + full_name.title() + "!"
print (message)

