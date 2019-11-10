#print the pets function
def print_list_of_pets():
    print("My pets are", pets)

#my list of pets
pets = ['dog', 'cat', 'rat', 'bird', 'iguana']

print_list_of_pets() #run the print the pets function

#insert a fish at index 3
pets.insert(3,"fish")

#run the print the pets function
print_list_of_pets() 

#insert a pony at index 0
pets.insert(0,"pony")

print_list_of_pets() #run the print the pets function

#append a hamster
pets.append("hamster")

print_list_of_pets() #run the print the pets function

#remove the rat
pets.remove("rat")

#run the print the pets function
print_list_of_pets()

#reverse the order of the list
pets.reverse()

#run the print the pets function
print_list_of_pets()

pets.sort()
print_list_of_pets()

newpetlist =pets.copy()
newpetlist.reverse()
print('My new copied sorted z-a list of pets is', newpetlist)

