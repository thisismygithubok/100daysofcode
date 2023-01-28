#Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names = name1+name2
names_lowercase = both_names.lower()

t = names_lowercase.count('t')
r = names_lowercase.count('r')
u = names_lowercase.count('u')
e = names_lowercase.count('e')

true = str(t+r+u+e)

l = names_lowercase.count('l')
o = names_lowercase.count('o')
v = names_lowercase.count('v')
e = names_lowercase.count('e')

love = str(l+o+v+e)

true_love = int(true+love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >=40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")