#6-7. People:
#6-1:Person
my_info={'first_name':'rishabh','last_name':'chopra','city':'new delhi','age':19,'height':"5'8",'school':'st. columabs','status':'single','DOB':'10/10/96'}
print(my_info['first_name'].title())
print(my_info['last_name'].title())
print(my_info['age'])
print(my_info['city'].title())
print(my_info['status'].title())
print(my_info['school'].title())
print(my_info['DOB'])
rohans_info={'first_name':'rohan','last_name':'chopra','city':'new delhi','age':23,'height':"5'11",'school':'springdales','status':'single','DOB':'03/03/93'}
manans_info={'first_name':'manan','last_name':'chopra','city':'new delhi','age':19,'height':"5'8",'school':'st. columbas','status':'ridhi','DOB':'22/02/1997'}
people=[my_info,rohans_info,manans_info]

for info in people:
    print("This is "+info['first_name'].title()+"'s information.")
    print("First Name: "+str(info['first_name'].title()))
    print("Last Name: "+str(info['last_name'].title()))
    print("Date of Birth: "+str(info['DOB']))
    print("School Name: "+str(info['school'].title()))
    print("City: " + str(info['city'].title()))
    print("Age: "+str(info['age']))
    print("Status: "+str(info['status'].title()))

#6-8:
lexus={'animal':'dog','owner':'rishabh','name':'lexus'}
mimi={'animal':'dog','owner':'rohan','name':'mimi'}
pets=[lexus,mimi]
for info in pets:
    print("This is "+info['name'].title()+"'s information")
    print("animal: "+info['animal'])
    print("owner's name: "+info['owner'].title())


#6-9:Favourite Places:
favourite_places={'rishabh':['delhi','pune','bombay'],'rohan':['switzerland','punjab','amritsar'],'nishi':['hawai','new york','sydney']}
print(favourite_places.items())
for name, places in favourite_places.items():
    print(name.title()+" would like to go to :"+"\n\t"+places[0].title()+"\n\t"+places[1].title()+
        " and\n\t"+places[2].title())

#6-10:Favourite Numbers:
#6-2:Favourite Numbers:
favourite_numbers={'rishabh':[10,11,12],
    'nishi':[26,27,28],
    'naresh':[23,24,25],
    'rohan':[3,4,5],
    'lexus':[26,27,28],}
print (favourite_numbers.values())
for name, numbers in favourite_numbers.items():
        print(name.title()+"'s favourite numbers are: ")
        print (numbers[0])
        print(numbers[1])
        print(numbers[2])

#6-11:Cities:
cities={'delhi':{'country':'india','aprx_population':'1 Cr.','fact':'The Red Fort is in Delhi',},
    'pune':{'country':'india','aprx_population':'50 Lakh','fact':"Durgas cold coffee is in Pune",},
    'bombay':{'country':'india','aprx_population':'1 Cr.','fact':'The Gateway of India is in Bombay'},}
print (cities.values()[0])

