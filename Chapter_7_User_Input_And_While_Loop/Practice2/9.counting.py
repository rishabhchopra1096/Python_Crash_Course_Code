c_n = 0

while c_n < 10:
    c_n += 1
    if c_n % 2 == 0:
        continue
    else:
        print(c_n)

# Starting from 0 , we add 1 and then
# We check weather the number is even or not.
# 1 is noteven , so it is printed.
# Loop starts again , 1 is added to 1 = 2
# If the number is even , we go back to the first line of the loop.
# The loop is entered as 2 < 10.
# We add 1 to 2 , which becomes 3.

