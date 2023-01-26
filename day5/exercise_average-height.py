# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split() #Student heights are an input of values, separated out into csv for a list
for n in range(0, len(student_heights)): #For each student height in the list, beginning with 0, max range of the # of items in the list
  student_heights[n] = int(student_heights[n]) #For each number in the student_heights list, convert it to an integer in list form
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#total_height = sum(student_heights) - easier way to do this...
total_height = 0 #Setting base height sum to 0
count = 0 #Setting base num of students to 0

for each_height in student_heights: #Iterating through the student_heights list
    total_height = total_height + each_height #Gathers total height by iterating through the student_heights list and summing them by grabbing the previous run's value
    #Easier written as total_height += each_height
#print(round(total_height))

for each_student in student_heights: #Iterating through the student heights list
    count += 1 #Takes the base count of 0 and adds 1 for each list item it goes through, essentially counting how many list entries there are
#print(count)

average_height = round(total_height/count) #Takes the average by rounding the total height / the count of students
print(average_height)

#total_height = total_height / len(student_heights)



