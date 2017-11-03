# it determines if the str occurs in string , or in  a substring
# of string if starting index beg and ending index end are given.
# Parameters:
# str : This specifies the string to be searched.
# beg : This is the starting index. by default its 0.
# end: This is the ending index , by default its equal to the length of the string.
# Return Value:
# Starting index if found , and -1 otherwise.
# Format:
# str.find(str, beg=0, end=len(string))

string = "My name is Rishabh."
print(string.find('Rish'))
#>>11
print(string[11:])

