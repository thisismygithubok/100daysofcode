# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split() #Student heights are an input of values, separated out into csv for a list
for n in range(0, len(student_heights)): #For each student height in the list, beginning with 0, max range of the # of items in the list
  student_heights[n] = int(student_heights[n]) #For each number in the student_heights list, convert it to an integer in list form
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#total_height = sum(student_heights)
total_height = 0

for each_height in student_heights:
    total_height = total_height + each_height
    #Easier written as total_height += each_height
total_height = total_height / len(student_heights)
print(round(total_height))


