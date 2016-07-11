from pprint import pprint as pp
import os

import requests

import namefile

NAME_FILE_URL = 'https://www.ssa.gov/oact/babynames/names.zip'
NAME_FILE = 'names.zip'


def main():

    if not os.path.exists(NAME_FILE):
        print('Downloading {}'.format(NAME_FILE_URL))
        download_file(NAME_FILE_URL)

    nf = namefile.Namefile(NAME_FILE)
    freq_table = nf.names_from_year('2015')
    pp(names_with_value(freq_table, 42))


def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename


def names_with_value(freq_table, value):
    ''' Return list of name frequency records that match the given value. '''
    return list(filter(lambda e: namecount(e.name) == value, freq_table))


def namecount(name):
    ''' Return total values of letters in a string. '''
    return sum(map(letter_value, name))


def letter_value(letter):
    ''' Return value of a letter where A=1, B=2, C=3, and so forth. '''
    assert len(letter) == 1
    assert letter.isalpha()
    return ord(letter.lower()) - ord('a') + 1


if __name__ == '__main__':
    main()
