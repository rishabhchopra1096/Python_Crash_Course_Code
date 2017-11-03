# #Start with some designs that need to be printed.
# unprinted_designs=['iphone case','robot pendant','dodecahedron']
# completed_models=[]
# #Stimulate printing each design till none are left.
# #Move each design to ccompleted_model after printing.
# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     print("Printing model: "+current_design.title())
#     completed_models.append(current_design.title())

# print("The following models have been printed:")
# for completed_model in completed_models:
#     print (completed_model)
# print ("And here is the list of completed models: ")
# print (completed_models)

# Now converting it into functions:
#printing models will only be used 1 time, the second time you
#need to use printing models, you have to remove the default value.
#That is why i removed the default value and changed it to the list
#completed models.
#Now see below what happends whyen i use the function twice.
#It will account for the previous designs also.

completed_models=[]
def printing_models(unprinted_designs,completed_models=completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("Printing model: "+current_design.title())
        completed_models.append(current_design.title())

print (completed_models)
def printed_models(completed_models=completed_models):
    print("The following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
    print("And here is the list of completed models: ")
    print (completed_models)

printing_models(['design1','design2','design3'])
printed_models()
printing_models(['desgin4','design5','design6'])
printed_models()





