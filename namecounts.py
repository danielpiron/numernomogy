def namecount(name):
    return sum(map(letter_value, name))


def letter_value(letter):
    assert len(letter) == 1
    assert letter.isalpha()
    return ord(letter.lower()) - ord('a') + 1
