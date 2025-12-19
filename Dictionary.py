# Igala (Kogi State) Dictionary

igala_to_english = {
    "oma": "child",
    "ata": "father",
    "iye": "mother",
    "ane": "food",
    "ojo": "house",
    "eje": "market",
    "oko": "farm",
    "ero": "clothes",
    "ule": "sleep",
    "ami": "water",
    "oka": "road",
    "oche": "sun",
    "uche": "work",
    "okojo": "money",
    "icho": "fire",
    "ene": "meat",
    "adu": "dog",
    "oma-ata": "son",
    "oma-iye": "daughter",
    "ejule": "friend"
}

# Create English to Igala dictionary automatically
english_to_igala = {value: key for key, value in igala_to_english.items()}

print("Igala ↔ English Dictionary (Kogi State Language)")
print("1. Igala to English")
print("2. English to Igala")
print("Type 'exit' to quit\n")

while True:
    choice = input("Choose an option (1 or 2): ").lower()

    if choice == "exit":
        print("Goodbye 👋")
        break

    if choice == "1":
        word = input("Enter an Igala word: ").lower()
        if word in igala_to_english:
            print("Meaning:", igala_to_english[word])
        else:
            print("Word not found.")

    elif choice == "2":
        word = input("Enter an English word: ").lower()
        if word in english_to_igala:
            print("Igala word:", english_to_igala[word])
        else:
            print("Word not found.")

    else:
        print("Invalid choice. Please enter 1 or 2.")
