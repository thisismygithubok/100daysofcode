#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total = input("What was the total? : $")

total_int = float(total)
per_person = round((total_int / 5 * 1.12),2) 

print(f"Each person owes: ${per_person}")

#Here's an expanded calc which asks how many people and the tip % as well.

total_2 = float(input("What was the total? : $")) #This takes the total and floats it, allowing decimals to carry over
people_2 = int(input("How many people? : ")) #This takes the people and keeps it as an int, rather than str needing re-converting
tip = int(input("What is the tip percentage? : ")) #This takes the tip and keeps it as an int, rather than str needing re-converting

tip_corrected = (tip / 100) + 1 #This takes the tip number, divides by 100 to give the decimal, and add 1, i.e. tip is 20%, 20/100 = .2 + 1 = 1.2
per_person = round((total_2 / people_2 * tip_corrected),2) #This rounds to 2 decimal places for any number, but won't show 2 if it's a whole number or only 1 decimal place, i.e. 24 or 24.1
rounded = "{:.2f}".format(per_person) #This rounds to 2 decimal places even if the total is a whole number.

print(f"Each person owes: ${rounded}") #Prints the result w/ a decimal place of 2, no matter the number.