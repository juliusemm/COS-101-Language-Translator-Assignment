hausa_dict = {
    'hello': 'Sannu',
    'goodbye': 'Sai anjama',
    'thank you': 'Musa',
    'water': 'Maa',
    'food': 'Abinci',
    'house': 'Gida',
    'father': 'Aba',
    'mother': 'Aya',
    'friend': 'Aboki',
    'work': 'Aiki',
    'school': 'Makaranta',
    'car': 'Mota',
    'tree': 'Itace',
    'book': 'Kitab',
    'pen': 'Alkalami',
    'man': 'Mutum',
    'woman': 'Mace',
    'child': 'Yaro',
    'eat': 'Ci',
    'run': 'Gudu'
}

word = input("Enter English word: ").lower()
print("Hausa:", hausa_dict.get(word, "Word not found"))