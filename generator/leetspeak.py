def transform(words):
    leet_map = {'a':'@','e':'3','i':'1','o':'0','s':'$','l':'1'}
    transformed = []

    for word in words:
        leet_word = ''.join([leet_map.get(c.lower(), c) for c in word])
        transformed.append(leet_word)

    return transformed
