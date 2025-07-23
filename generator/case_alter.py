import random

def alter_cases(words):
    variants = []

    for word in words:
        variants.append(word.lower())
        variants.append(word.upper())
        variants.append(word.capitalize())
        variants.append(''.join(random.choice([c.lower(), c.upper()]) for c in word))

    return variants
