#Index Errors

states_of_america = [
    "Georgia",
    "Kentucky",
    "Indiana",
    "Michigan",
    "South Carolina"
]

print(len(states_of_america)) #Prints how many items are in the list
print(states_of_america[4]) #Selects the last item from the list
num_of_states = len(states_of_america) #Counts how many items are in the list
#print(states_of_america[num_of_states]) #This is an index out of range error, b/c there are only 5 items in the list, can't select a 6th item.
print(states_of_america[num_of_states - 1]) #Gets rid of the index out of range error


#Nested Lists

dirty_dozen = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears"
]
vegetables = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery",
    "Potatoes"
]

dirty_dozen = [fruits, vegetables] #A list of multiple lists

print(dirty_dozen) #Prints out the nested lists