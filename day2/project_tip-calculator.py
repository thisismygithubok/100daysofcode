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

total_2 = input("What was the total? : $")
people_2 = int(input("How many people? : "))
tip = int(input("What is the tip percentage? : "))

total_int_2 = float(total_2)
tip_corrected = (tip / 100) + 1
per_person = round((total_int_2 / people_2 * tip_corrected),2)

print(f"Each person owes: ${per_person}")