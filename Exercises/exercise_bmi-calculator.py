#BMI Calculator
#BMI = weight(kg) / height^2(m^2)

height = input("How tall are you in meters? : ")
weight = input("How much do you weigh in kg? : ")

int_weight = float(weight) #Takes the user's weight and floats, accepting decimals
int_height = float(height) #Takes the user's height and floats, accepting decimals

bmi = (int_weight / (int_height**2)) #Caculates for BMI using provided user input numbers
bmi_int = int(bmi) #Calculates for BMI and converts to int, i.e. rounding down to the closest whole number

print(bmi_int) #Prints the result, rounded BMI number