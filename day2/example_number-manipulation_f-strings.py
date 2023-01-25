#Number Manipulation and F Strings


#Number Manipulation

print(int(8/3)) #This rounds DOWN the result to the closest whole number
print(round(8/3)) #This rounds UP the result to the closest whole number
print(round(8/3, 2)) #This rounds to the 2nd digit, i.e. 2.67
print(8//3) #Floor division, which converts directly to an int directly rather than float

result = 4/2 #This is just doing 4/2 into a variable to be used later
result /= 2 #This continues the math, dividing "result" by 2 again
print(result) #Takes the final result, 4 / 2 / 2 = 1

score = 0 #Set score as 0
score += 1 #Take score and add 1
print(score) #Print final score of 1


#F Strings

score = 0 #Int
height = 1.8 #Int
isWinning = True #Boolean
print(f"Your score is : {score}, your height is : {height}m, and are you winning? : {isWinning}.") #An f string allows you to directly utilize int values by converting them into strings without the need to do the str() operation.


