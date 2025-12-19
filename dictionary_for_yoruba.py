yoruba_dict = {
    'hello': 'E kú',
    'goodbye': 'Ó dà bó',
    'thank you': 'E seun',
    'water': 'Omi',
    'food': 'Oúnje',
    'house': 'Iilé',
    'father': 'Bàbá',
    'mother': 'Ìyá',
    'friend': 'Ọ̀rẹ́',
    'work': 'Iṣẹ́',
    'school': 'Ilé-ìwé',
    'car': 'Ọkọ́',
    'tree': 'Igi',
    'book': 'Ìwé',
    'pen': 'Ìkọ',
    'man': 'Ọkúnrin',
    'woman': 'Obìnrin',
    'child': 'Ọmọ',
    'eat': 'Jẹun',
    'run': 'Sáré'
}

word = input("Enter English word: ").lower()
print("Yoruba:", yoruba_dict.get(word, "Word not found"))
