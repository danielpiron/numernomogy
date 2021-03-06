import numernomogy as ng
import namefile
import unittest


class TestNameFileReader(unittest.TestCase):

    def test_line_reader(self):
        expected = namefile.NameFrequency(1234, 'Daniel', namefile.Gender.male)
        self.assertEqual(expected, namefile.read_record('Daniel,M,1234'))

    def test_line_reader_arbitrary_whitespace(self):
        expected = namefile.NameFrequency(4321, 'Amy', namefile.Gender.female)
        self.assertEqual(expected, namefile.read_record(' Amy,  F, 4321\n'))


class TestNameCounts(unittest.TestCase):

    def test_namecount_empty_string(self):
        self.assertEqual(0, ng.namecount(''))

    def test_namecount_lowercase(self):
        self.assertEqual(42, ng.namecount('alex'))
        self.assertEqual(42, ng.namecount('evan'))

    def test_namecount_case_insensitivity(self):
        self.assertEqual(42, ng.namecount('Alex'))
        self.assertEqual(42, ng.namecount('Evan'))

    def test_namecount_assert_on_numbers(self):
        with self.assertRaises(AssertionError):
            ng.namecount('4real')


if __name__ == '__main__':
    unittest.main()
