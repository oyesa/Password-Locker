import unittest
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
