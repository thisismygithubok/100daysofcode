#Calculating how long you have left in life based on the maximum age of 90.

age = input("How old are you? : ")

int_age = int(age)
days =  (90 * 365) - (int_age * 365) #Calculates days remaining until you turn 90 based on your input age in years.
weeks = (90 * 52) - (int_age * 52) #Calculates weeks remaining until you turn 90 based on your input age in years.
months = (90 * 12) - (int_age * 12) #Calculates months remaining until you turn 90 based on your input age in years.

print(f"You have {days} days, {weeks} weeks, and {months} months left.") #Prints out the result by using an f-string to directly convert the integrers into strings.