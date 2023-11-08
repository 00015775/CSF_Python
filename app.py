
































































































































































































































































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

