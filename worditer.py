class WordIterator(object):
    """
    Split the given text at white spaces,
    and return the parts one by one.
    """

    def __init__(self, text):
        self._words = text.split()

    def next(self):
        if len(self._words) > 0:
            return self._words.pop(0)
        else:
            raise StopIteration

    def __iter__(self):
        return self


## test intended usage
  
import unittest

class WordIteratorTest(unittest.TestCase):

    def test_word_sequence(self):
        witer = WordIterator("word by word iteration")
        words = list(witer)
        self.assertEqual(words, ['word', 'by', 'word', 'iteration'])

    def test_empty_text(self):
        witer = WordIterator("")
        no_words = list(witer)
        self.assertTrue(len(no_words) == 0)

    def test_multiple_whitespace(self):
        witer = WordIterator("a  text   with multiple spaces  in   it")
        self.assertEqual(list(witer),
                         ['a', 'text', 'with', 'multiple', 'spaces', 'in', 'it'])


if __name__ == "__main__":
    unittest.main()
