#Adding Even Numbers

total = 0 #set base total as 0

for each in range(0,101,2): #for each number in the range 0 through 100, step every 2, i.e. select all the even numbers. This is important to start at 0, if you start at 1, it grabs all odd numbers.
    total += each
print(total)
