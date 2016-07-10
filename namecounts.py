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

    import pprint
    import zipfile
    with zipfile.ZipFile(NAME_FILE) as zf:

        freq_table = []
        for line in zf.open('yob2015.txt'):
            nf = namefile.read_record(line.decode())
            freq_table.append(nf)

        forty_twos = filter(lambda e: namecount(e.name) == 42, freq_table)
        pprint.pprint(list(forty_twos))
