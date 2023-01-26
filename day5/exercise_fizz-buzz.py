#Fizz Buzz Interview Question

for each in range(1,101):
    if each % 3 == 0 and each % 5 == 0:
        each = "FizzBuzz"
        print(each)
    elif each % 3 == 0:
        each = "Fizz"
        print(each)
    elif each % 5 == 0:
        each = "Buzz"
        print(each)
    else:
        print(each)