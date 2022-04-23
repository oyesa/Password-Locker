import unittest    #import unittest module to construct and run tests
from user import User  #import user class
from user import Details #import details class


class TestClass(unittest.TestCase):

    """
    Test class 
    """
    def setUp(self):

        """
        First run method before other test methods
        """
        self.new_user = User('OyesaOluchina','NotI793fl0')

    def test_init(self):

        """
        test if object has been initialized
        """
        self.assertEqual(self.new_user.username,'OyesaOluchina')
        self.assertEqual(self.new_user.password,'NotI793fl0')
