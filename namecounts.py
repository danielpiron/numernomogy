from collections import namedtuple
from enum import Enum
import os
import re
import zipfile

NAME_FILE = os.path.expanduser('~/Downloads/names.zip')


def namecount(name):
    return sum(map(letter_value, name))


def letter_value(letter):
    assert len(letter) == 1
    assert letter.isalpha()
    return ord(letter.lower()) - ord('a') + 1

CRE_YOB_DATAFILE = re.compile('yob\d{4}\.txt')


class Gender(Enum):
    female = 'f'
    male = 'm'

NameFrequency = namedtuple('NameFrequency', 'frequency name gender')


if __name__ == '__main__':

    gender_translation = {
        'F': Gender.female,
        'M': Gender.male
    }

    with zipfile.ZipFile(NAME_FILE) as zf:

        freq_table = []
        for line in zf.open('yob2015.txt'):
            name, gender, freq = line.decode().strip().split(',')
            nf = NameFrequency(freq, name, gender_translation[gender])
            freq_table.append(nf)
