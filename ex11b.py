import unittest

def is_prime(number):
    """Return True if *number* is prime."""

    if not isinstance(number, int) or number is True or number is False:
        # True and False in python inherits from `int`!
        raise ValueError("Only integers can be checked for primality")

    # This rule catches multiple cases:
    #
    # * negative numbers and 0, because the definition of a prime
    #   number is valid only for "Natural numbers", that is, only
    #   strictly positive integers
    #
    # * 1, because it has infinite possible decompositions: 1, 1^2,
    #   1^3...
    if number <= 1:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False

    return True

class PrimeTestCase(unittest.TestCase):
    def test_is_four_not_prime(self):
        """Is four successfully determined to be composite?"""
        self.assertFalse(is_prime(4))

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

    def test_is_one_not_prime(self):
        """Is one correctly determined not to be prime?"""
        self.assertFalse(is_prime(1))
    
    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg="%d should not be prime" % index)

    def test_string_raises_an_exception(self):
        """Does an invalid value raises an error?"""
        with self.assertRaises(ValueError):
            is_prime("blablabla")

    def test_False_raises_an_exception(self):
        with self.assertRaises(ValueError):
            is_prime(False)

    def test_True_raises_an_exception(self):
        with self.assertRaises(ValueError):
            is_prime(True)



if __name__ == "__main__":
    unittest.main()
