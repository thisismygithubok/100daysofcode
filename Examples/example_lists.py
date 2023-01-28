#Lists

states_of_america = [
    "Georgia",
    "Kentucky",
    "Indiana",
    "Michigan",
    "South Carolina"
]

print(states_of_america[1]) #Grabs 2nd item in list, index starts from 0
print(states_of_america[-1]) #Grabs last item in list, - allows you to query backwards

states_of_america[1] = "Kintucky" #Modifies value from called list value

print(states_of_america[1]) #Printing that modified value

states_of_america.append("Stevenville") #Append value to end of list

print(states_of_america[-1]) #Calling that newly appended value from end of list

states_of_america.extend(["Ainslietown","Maxville"]) #Append multiple items to end of list via new list

print(states_of_america) #Printing out those newly appended values from the extend operation