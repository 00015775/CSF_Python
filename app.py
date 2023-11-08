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


