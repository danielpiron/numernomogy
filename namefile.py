from collections import namedtuple
from enum import Enum
import re
import zipfile

CRE_YOB_DATAFILE = re.compile('yob\d{4}\.txt$')

NameFrequency = namedtuple('NameFrequency', 'frequency name gender')


class Gender(Enum):
    female = 'f'
    male = 'm'


class YearDataNotAvailableError(Exception):
    pass


class Namefile:

    def __init__(self, filepath):
        self._zip = zipfile.ZipFile(filepath)

    def names_from_year(self, year):
        freq_table = []
        for line in self._zip.open(self._year_data_filename(year)):
            nf = read_record(line.decode())
            freq_table.append(nf)
        return freq_table

    @staticmethod
    def _year_data_filename(year):
        return 'yob{0}.txt'.format(year)


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
