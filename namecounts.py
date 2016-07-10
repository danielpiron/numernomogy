import os
import namefile

NAME_FILE = os.path.expanduser('~/Downloads/names.zip')


def namecount(name):
    return sum(map(letter_value, name))


def letter_value(letter):
    assert len(letter) == 1
    assert letter.isalpha()
    return ord(letter.lower()) - ord('a') + 1


if __name__ == '__main__':
    from pprint import pprint as pp
    nf = namefile.Namefile(NAME_FILE)
    freq_table = nf.names_from_year('2015')
    forty_twos = filter(lambda e: namecount(e.name) == 42, freq_table)
    pp(list(forty_twos))
