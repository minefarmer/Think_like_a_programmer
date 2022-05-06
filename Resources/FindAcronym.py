

phrase = input("Enter a phrase: ")

phrase = phrase.strip()

phrase = phrase.upper()

words = phrase.split(" ")

letters = []
for word in words:
    letters.append(word[0])

acronym = ''.join(letters)

print(acronym)





