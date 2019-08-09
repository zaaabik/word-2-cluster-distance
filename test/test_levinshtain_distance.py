import unittest

from ClusterDistance import levenshtein_distance


class TestStringMethods(unittest.TestCase):
    def test_empty_string_to_non_empty_distance(self):
        empty_string = ''
        non_empty_string = 'aAfvr56tb sdfs43'
        dist = levenshtein_distance(non_empty_string, empty_string)
        self.assertEqual(dist, len(non_empty_string))

    def test_empty_strings_distance(self):
        empty_string1 = ''
        empty_string2 = ''
        dist = levenshtein_distance(empty_string1, empty_string2)
        self.assertEqual(0, dist)

    def test_string_without_element_distance(self):
        first_string = 'abcde'
        second_string = 'abde'
        dist = levenshtein_distance(first_string, second_string)
        self.assertEqual(1, dist)


if __name__ == '__main__':
    unittest.main()
