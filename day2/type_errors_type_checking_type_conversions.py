#Type Errors

#len(1234) #Type error, can't get length on type int
name = len(input("What is your name? : ")) #Just gets user input for name and counts characters as an int
#print ("Your name has " +name+ "characters.") #This does not work due to the type being int, not a string


#Type Checking

print(type(name)) # Tells us what type of class the name count is, int.


#Type Conversions

str_name_char = str(name) #This converts the int from name into a string so it can be printed
print("Your name has "+str_name_char+" characters.") #This prints out the result properly after the number is converted into a string

a = str(123) #This converts an int into a string easily
print(type(a)) #This shows it's now a type string

b = float(123) #This is a float type
print(type(b)) #This prints that it is a float type

print(70+float("100.5")) #This takes 70 and adds the value of the float type b/c the "100.5" is converted to a float type in the bracket

print(str(70)+str(100)) #This prints 70100 b/c the types are both strings

