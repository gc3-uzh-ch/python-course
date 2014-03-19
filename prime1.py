import unittest

def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(number):
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
    
    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg="%d should not be prime" % index)

if __name__ == "__main__":
    unittest.main()
