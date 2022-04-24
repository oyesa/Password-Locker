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

    def test_save_many_accounts(self):

        """
        test to check if we can save multiple detail objects to details list
        """
        self.new_detail.save_details()
        test_detail = Details("Twitter", "OyesaOluchina", "Mal93isa") 
        test_detail.save_details()
        self.assertEqual(len(Details.details_list),2)

    def test_delete_detail(self):

        """
        test method to test if we can remove an account's details saved in details_list
        """
        self.new_detail.save_details()
        test_detail = Details("Twitter", "OyesaOluchina", "Mal93isa")
        test_detail.save_details()

        self.new_detail.delete_details()
        self.assertEqual(len(Details.details_list),1)

    def test_find_detail(self):

        """
        test to check whether detail entry can be found by account name 
        """
        self.new_detail.save_details()
        test_detail = Details("Twitter", "OyesaOluchina", "Mal93isa") 
        test_detail.save_details()

        the_detail = Details.find_detail("Twitter")

        self.assertEqual(the_detail.account,test_detail.account)

    def test_detail_exist(self):

        """
        test to check whether we can or cant find the user detail (returns boolean) 
        """
        self.new_detail.save_details()
        the_detail = Details("Twitter", "OyesaOluchina", "Mal93isa")  
        the_detail.save_details()
        detail_is_found = Details.if_detail_exists("Twitter")
        self.assertTrue(detail_is_found)

    def test_display_all_saved_details(self):

        """
        method to display all details saved by user
        """

        self.assertEqual(Details.display_details(),Details.details_list)

    if __name__ == '__main__':
     unittest.main()
