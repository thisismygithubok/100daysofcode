#Calculating how long you have left in life based on the maximum age of 90.

age = input("How old are you? : ")

int_age = int(age)
days =  (90 * 365) - (int_age * 365) #Calculates days remaining until you turn 90 based on your input age in years.
weeks = (90 * 52) - (int_age * 52) #Calculates weeks remaining until you turn 90 based on your input age in years.
months = (90 * 12) - (int_age * 12) #Calculates months remaining until you turn 90 based on your input age in years.

print(f"You have {days} days, {weeks} weeks, and {months} months left.") #Prints out the result by using an f-string to directly convert the integrers into strings.

#Above is how I did it, below is the shown way, which is more concise and makes more sense.
 
years = 90 - int_age #Takes the int'd age subtracted from 90 to get years remaining.
days = years * 365 #Takes those remaining years * 365 to get days remaining.
weeks = years * 52 #Takes those remaining years * 52 to get weeks remaining.
months = years * 12 #Takes those remaining years * 12 to get months remaining.

print(f"You have {days} days, {weeks} weeks, and {months} months left.") #Printed result is same.