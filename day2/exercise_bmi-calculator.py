#BMI Calculator
#BMI = weight(kg) / height^2(m^2)

height = input("How tall are you in meters? : ")
weight = input("How much do you weigh in kg? : ")

int_weight = float(weight) #Takes the user's weight and floats, accepting decimals
int_height = float(height) #Takes the user's height and floats, accepting decimals

bmi = int(int_weight / (int_height**2)) #Calculates for BMI and converts to int, i.e. rounding down to the closest whole number

print(bmi) #Prints the result, rounded BMI number