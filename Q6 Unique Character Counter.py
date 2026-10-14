sentence = input("Enter a long sentence: ")
unique_characters = set()
for char in sentence:
    if not char.isspace():
        unique_characters.add(char)
print("Unique characters:", unique_characters)
print("Total unique characters:", len(unique_characters))