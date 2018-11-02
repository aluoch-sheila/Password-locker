import unittest 
from password import Password 

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the password class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("first_name","last_name","password","email")



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"first_name")
        self.assertEqual(self.new_password.last_name,"last_name")
        self.assertEqual(self.new_password.password,"password")
        self.assertEqual(self.new_password.email,"email")

   
    def test_save_password(self):
        """
        test_save_password test case to test if the password object saved into the password list
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list),1)

    def tearDown(self):
        """
        tearDown method that cleans up after each test has run
        """

        Password.password_list = []

    def test_save_multiple_password(self):
        '''
        test_save_multiple_password to check if we can save multiple password
        objects to our password_list
        '''
        self.new_password.save_password()
        test_password = Password("Test","user","password","email") 
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)


    def test_delete_password(self):
        '''
        test_delete_password to test if we can remove a password from our password list
        '''
        self.new_password.save_password()
        test_password = Password("Test","user","password","email")
        test_password.save_password()

        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1) 

    def test_find_password_by_number(self):
        '''
        test to check if we can find a password by phone number and display information
        '''

        self.new_password.save_password()
        test_password = password("Test","user","0711223344","test@user.com")
        test_password.save_password()

        found_password = Password.find_by_password("password")

        self.assertEqual(found_password.email,test_password.email)   
      

if __name__ == '__main__':
    unittest.main()

      