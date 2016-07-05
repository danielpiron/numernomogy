def namecount(name):
    return sum([ord(letter) - ord('a') + 1 for letter in name.lower()])
