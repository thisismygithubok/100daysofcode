#Functions

# def greet ():
#     print("Hi, how are you?")
#     print("What is your name?")
#     print("Where do you live?")

# greet()

#Functions with inputs

# def greeting(name):
#     print(f"Hello, {name}")
#     print(f"How are you today {name}?")

# greeting("Steven")

# name = input("What is your name?: ")

# def greeting(name): #parameter is name, argument is the DATA of the parameter, in this case, parameter = name, argument = the user's input
#     print(f"Hello, {name}")
#     print(f"How are you today {name}?")

# greeting(name)

#Functions with more multiple inputs

name = input("Hello, what is your name? ")
location = input("Where do you live? ")

def greet_with(name,location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

# greet_with(name,location) #Example - position matters b/c this is positional arguments
greet_with(location=location,name=name) #Example - positioning doesn't matter if you use keyword arguments