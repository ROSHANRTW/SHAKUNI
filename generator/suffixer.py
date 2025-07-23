def append_suffix(words, suffix):
    if not suffix:
        return words

    suffixes = suffix.split()
    new_words = []

    for word in words:
        new_words.append(word)  
        for s in suffixes:
            new_words.append(word + s)       
            new_words.append(s + word)       

    # Also include suffixes alone
    for s in suffixes:
        new_words.append(s)

    return list(set(new_words))  
