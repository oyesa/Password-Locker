import unittest    #import unittest module to construct and run tests
from user import User  #import user class
from user import Details #import details class


class TestClass(unittest.TestCase):

    """
    Test class 
    """
    def setUp(self):

        """
        first run method before other test methods
        """
        self.new_user = User('OyesaOluchina','NotI793fl0') # create contact object

    def test_init(self):

        """
        test if object has been initialized properly
        """
        self.assertEqual(self.new_user.username,'OyesaOluchina')
        self.assertEqual(self.new_user.password,'NotI793fl0')

    def test_save_user(self):

        """
        test case for saving new user instance to User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestDetails(unittest.TestCase):

    """
    A test class for details class
    """ 
    def setUp(self):

        """
        first run method before other details test methods
        """
        self.new_detail = Details('Gmail','Oyesa_Oluchina','ru7Kit33')

    def test_init(self):

        """
         test if object has been initialized properly
        """
        self.assertEqual(self.new_detail.account,'Gmail')
        self.assertEqual(self.new_detail.userId,'Oyesa_Oluchina')
        self.assertEqual(self.new_detail.password,'ru7Kit33')

    def save_detail_test(self):

        """
        test case if detail object has been saved to details list.
        """
        self.new_detail.save_details()
        self.assertEqual(len(Details.details_list),1)   

    def tearDown(self):

        """
        method that does clean up after each test case has run.
        """
        Details.details_list = []


    if __name__ == '__main__':
     unittest.main()
