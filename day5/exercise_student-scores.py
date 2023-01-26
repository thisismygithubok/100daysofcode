# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

score = 0 #Set base score

for each in student_scores: #Iterate through the list of int score values
    if each > score: #See if current value is higher than base score (0)
        score = each #Set the value of score to that new higher value.
print(f"The highest score in the class is: {score}") #Print the highest value.
