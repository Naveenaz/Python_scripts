import unittest

from replace_text import replacer


class ReplacerTests(unittest.TestCase):
    def test_single(self):
        self.assertEqual(
            ["no,the,answer,is,no", True,
             "yes: replaced 2 times"],
            replacer("yes,the,answer,is,yes", ["yes"], ["no"])
        )

    def test_many(self):
        self.assertEqual(
            ["no,a,answer,is,no", True,
             "yes: replaced 2 times" +
             "the: replaced 1 time" +
             "twelve: replaced 0 times"],
            replacer("yes,the,answer,is,yes",
                     ["yes", "the", "twelve"], ["no", "a", "thirteen"])
        )

    def test_len_not_equal(self):
        self.assertEqual(
            ['yes,the,answer,is,yes', False, 'List lengths do not match'],
            replacer("yes,the,answer,is,yes", ["yes", "the"], ["no"])
        )

    # Following tests are added by Naveen Zunjarwad.
    # Test to check what will happen if user inputs empty strings, where length of two input strings are equal i.e 0
    def test_empty_lists_string(self):
        self.assertEqual(
            [ True, ''],
            replacer('', [], [])
        )

    # Test to check what will happen if user inputs empty lists, where length of two input strings are equal i.e 0
    def test_empty_lists(self):
        self.assertEqual(
            ["no,the,answer,is,no", True,
             ""],
            replacer("no,the,answer,is,no",
                     [], [])
        )

    #Test to check what will happen if user inputs same word again to replace like ["yes", "yes"]. Expected output should show last replacements.
    def test_repeat_string(self):
        self.assertEqual(
            ["no,the,answer,is,no", True,
             "yes: replaced 0 times"],
            replacer("yes,the,answer,is,yes",
                     ["yes", "yes"], ["no", "yes"])
        )

   #Note even though word "yes" present in "yesyes,the,answer,is" , we do not replace, because "yes" is not whole word.
    def test_whole_word(self):
        self.assertEqual(
            "yesyes,the,answer,is",
            replacer("yesyes,the,answer,is",
                     ["yes", "the", "twelve"], ["no", "a", "thirteen"])
        )

if __name__ == '__main__':
    unittest.main()