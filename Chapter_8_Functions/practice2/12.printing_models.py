# Start with some designs that need to be printed.
unprinted_designs = ['iphone case','robot penant','dodecahedron']
completed_models = []

#Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

'''while unprinted_designs:
    current_design = unprinted_designs.pop(0)
    #Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)'''

#Display all completed models.
'''print("The following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
'''

'''Converting the above code to a function'''
# What all does it use?
# 2 lists : unprinted_design and completed_models

def print_models(unprinted_designs,completed_models):
    #Simulate printing each design, until none are left.
    # Move each design to completed_models after printing.
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        #Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models = completed_models):
    """Shows all the models that were printed."""
    print("The following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

print(print_models(unprinted_designs,completed_models))
print(completed_models)




