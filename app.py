# convert = int(input("Enter the decimal number: "))
#
# binary = bin(convert)
# octal = oct(convert)
# hexadecimal = hex(convert)
#
# print("Binary: ", binary)
# print("Octal: ", octal)
# print("Hexadecimanl: ", hexadecimal)

#example of functions
# def minus(x, y):
#     return x - y
#
# minus(10, 4)

# def divide(x , y):
#     return x // y
#
# divide(100, 24)
#
# def multiply(a, b):
#     return int(a / b)
#
# cwMark = 76
# cwSimilarity = 3
#
# print(multiply(cwMark, cwSimilarity))

# def work():
#     print(12345) #this is a void function that does not return any value


print("Ny name is Eminem\nI do what i want\n")

counter = 0

def increment():
    global counter
    counter += 1

print("Initial counter value: ", counter)

increment()
print("Counter value after increment: ", counter)

increment()
print("Counter value after another increment: ", counter)


result = 0

def caculate_average(numbers):
    global result
    total = sum(numbers)
    average = total / len(numbers)
    result = average

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

caculate_average(numbers)

print(result)



login_valid = False


def more_or_less(x, y):
    if x > y:
        print("x is greater than y")
    else:
        if x < y:
            print("y is greater than x")
        else:
            print("x and y are equal")


more_or_less(12, 14)

def login(username, email, password):
    global login_valid
    if username == "GoodWill" and email == "GoodWill@gmail.com" and password == "1234":
        login_valid = True
    else:
        login_valid = False

username_input = input("Enter username: ")
email_input = input("Enter email: ")
password_input = input("Enter password: ")

login(username_input, email_input, password_input)

if login_valid:
    print("Login Successful!😄")
else:
    print("Invalid username and password 😞")

calc = 0

def more_less(x , y):
    global calc
    if x > y:
        total = x - y
        print(f"First number is greater than the Second by {total}")
    else:
        if x < y:
            total = y - x
            print(f'Second number is greater than the First number by {total}')
        else:
            print("Both numbers are equal")

#\n makes a new line

x = int(input("First number:\n"))
y = int(input("Second number:\n"))

more_less(x, y)

print("Choose converting options")
conversion = input("(B)bin, (O)oct or (H)hex: ").lower()



if conversion == "b":
    convert = input("Enter your number: ")
    total = bin(int(convert))
    print("Your number in binary: ", total)
elif conversion == "o":
    convert = input("Enter your number: ")
    total = oct(int(convert))
    print("Your number in oct: ", total)
elif conversion == "h":
    convert = input("Enter your number: ")
    total = hex(int(convert))
    print(f"You number in oct: {total}")
else:
    print("Invalid input, please choose the given options")


def countdown(timer):
    if timer <= 0:
        print("Time Off!")
    else:
        print(timer)
        countdown(timer - 1)



countdown(10)

x1 = 1

while x1 <= 10:
    print(x1)
    x1 += 1

print("Time Off")



def countdown(number):
    while number > 0:
        print(number)
        number -= 1
    print("Countdown complete!")

def countup(number):
    while number < 0:
        print(number)
        number += 1
    print("Countup completer!")

number = int(input("Enter number: "))

if number > 0:
    countdown(number)
elif number < 0:
    countup(number)
else:
    print("Input 0 invalid")



