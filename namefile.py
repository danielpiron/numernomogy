from collections import namedtuple
from enum import Enum
import re

CRE_YOB_DATAFILE = re.compile('yob\d{4}\.txt$')

NameFrequency = namedtuple('NameFrequency', 'frequency name gender')


class Gender(Enum):
    female = 'f'
    male = 'm'


def read_record(line):
    ''' Translates a line from a name file into `NameFrequency` record '''
    name, gender, freq = re.split('\s*,\s*', line.strip())
    return NameFrequency(int(freq), name, decode_gender(gender))


def decode_gender(gender_key):
    gender_translation = {
        'F': Gender.female,
        'M': Gender.male
    }
    return gender_translation[gender_key.upper()]
