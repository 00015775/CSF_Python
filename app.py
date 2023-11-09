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


write = int(input("From: "))
to = int(input("To: "))

while write <= to:
    print(write)
    write += 1


i = 1

while i <= 10:
    print(i * '*')
    i += 1
j = 10
while j >= 1:
    print(j * '*')
    j -= 1

num = int(input("Write: "))

def down(num):
    while num > 0:
        print(num)
        num -= 1
    print("Done")

down(num)

while True:
    end = input("> ").lower()
    if end == 'done':
        break
    else:
        print("Invalid Value")
print("Work terminated")

attempts = 3
count = 0
secret_number = 9

while count < attempts:
    guess = int(input("Guess number: "))
    count += 1
    if guess == secret_number:
        print("You Won game!")
        break
    elif count == attempts:
        print("Game Over.")
    else:
        print("Sorry, incorrect!")
 # by default \n is used to make a new line, with end='' new code will be on the same line with the previous code
print("Hello!", end="")
print("World")
print("Very exicted about my job!")

# range function

n = 10

for scroll in range(n):
    for xcode in range(scroll):
        print('* ', end='')
    print("")


num = range(10, -1, -1)

for x in num:
    print("* " * x)

#shared to GitHub

test = input("Input number: ")

try:
    def test_is_valid(test):
        check = isinstance(int(test), int)
        print(check)
    test_is_valid(test)

except ValueError:
    print("Invalid Value")

index = 0
letter = input("Enter Word: ")

while index < len(letter):
    word = letter[index]
    print(word)
    index += 1

word = 'NDHRDS'
ending = 'ack'

for words in word:
    print(words + ending)


text = "Hello locky!"
print(text.find("lo", 5))

word = input("Word: ")
letter = input("Letter: ")
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] ==  letter:
            return index
        index += 1

print(find(word, letter))

text = input("Num: ")
search = input("Find: ")
print(text.find(search))
# counter of a specific letter

word = input("Word: ")
letter = input("Letter: ")
count = 0

for text in word:
    if text == letter:
        count += 1
print(f"Result: {count}")

message1 = input("Message1: ").lower()
message2 = input("Message2: ").lower()

def is_the_same(message1, message2):
    while isinstance((message1 and message2), str):
        if message1 == message2:
            print("True")
            break
        else:
            print("False")
            break

is_the_same(message1, message2)

eng2uz = {
    "one": 'bir',
    'two': 'ikki',
    'three': 'uch',
    'four': 'tort'
}
one = input("Translate: ")
if one == "one":
    print("result: ", eng2uz['one'])
else:
    print('invalid')

# below is to check if certain key is inside of dictionary
print('one' in eng2uz)

# below is the check if certain value is insde of dictionary

valve = eng2uz.values()
print('uch' in valve)

final_marks = {
    'CSF': 75,
    'FUNPRO': 80,
    'IMOB': 57,
    'ISDS': 63
}

option = input("Choose Modules: ").upper()

if option == 'CSF':
    print(final_marks['CSF'])
elif option == 'FUNPRO':
    print(final_marks['FUNPRO'])
elif option == 'IMOB':
    print(final_marks['IMOB'])
elif option == 'ISDS':
    print(final_marks['ISDS'])

average = input(f"Calculate average of all modules?\nY(yes) or N(no): ").upper()

if average == 'Y':
    total = sum(final_marks.values()) / len(final_marks)
    print(total)
elif average == 'N':
    pass
else:
    print("Invalid Value")


h = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(h.get('f', 0))

csf = {
    'cw1_weight': 0.4,
    'cw1_mark': 79,
    'exam_weight': 0.6,
    'exam_mark': 65
}
a = csf.get('cw1_mark') * csf['cw1_weight']
b = csf['exam_mark'] * csf['exam_weight']
c = a + b
d = c / len(csf)
print(f"Final mark: {d}")


#this is how to create a tuple with a single element
#with brackets it is going to be a string not a tuple
#for a tuple it is not must to have brackets
t1 = 2, 3, 4, 7
print(type(t1))
#type tuple.

t2 = 'work'
print(tuple(t2))

print((1, 123, 4) < (1, 2, 4))

print((14555, 10, 'Samarkand')<(15775, 19, 'Tashkent'))

a, b, c = 1, 2, 3
print(a + b + c)

email = 'james@gamil.com'

username, gmail = email.split('@')
print(username, gmail)

try:
    one = int(input("1: "))
    two = int(input("2: "))

    def cal(one, two):
        calcul = one//two
        return calcul


    print("division: ", cal(one, two))
except ValueError:
    print("Invalid input")


result = divmod(10, 3)
print(result)


def write(*work):
    print(work)


write(1, 2, 56, 'work')

dad = 'good'
mom = [1, 2, 3, 4]
me = zip(dad, mom)
# print(list(me))
for wire in me:
    print(wire)

print('\n')

for index, word in enumerate('abs', 0):
    print(index, word)
print('\n')

my_tuple = ('a', 'b', 'c', 'd', 'e')
for i in enumerate(my_tuple):
 print(i)

print('\n')

for work, yea in enumerate("job"):
    print(work, yea)

print(dict(zip('WOK', range(3))))

print(dict())

d = {'d': 1, 'b': 2, 'c': 3}

t = d.items()
print(t)

wok = [('c', 1), ('g', 2), ('f', 3)]
print(dict(wok))

jj = 1, 2, 4, 5, 6, 7
kk = 'absdefg'

print(list(zip(kk, jj)))

meme = {'name': 'Mike', 'work': 'Logistics', 'status': 'single'}

for kaggle, value in meme.items():
    print(kaggle, value)

def add(a = 0, b= 0, c= 0):
    sum = a + b + c
    print(f'Sum: {sum}')
add()





