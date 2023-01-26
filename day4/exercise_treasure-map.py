# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0]) #This takes your user input 1st number and keeps it as an int
vertical = int(position[1])  #This takes your user input 2nd number and keeps it as an int

#This takes your 2nd user input number, the row you wanted, and selects that on the map list, i.e. if you chose "23", it takes 3 - 1 = 2 to tell it the last item in the map row list, row 3.
#This then stores that value as selected_row, so now selected_row = 3
selected_row = map[vertical - 1] 

#This then tells the selected row list which column you want to replace with the value "X", i.e. you chose "23", so it takes row3[(2-1)=1], telling it to place it in the first column
#At this point, you've now replaced the row and list position you wanted in that row with the value "X", so when it prints that row, it replaces the desired list index w/ an "X"
selected_row[horizontal - 1] = "X" 

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")