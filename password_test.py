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

if __name__ == '__main__':
    unittest.main()

def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = password("Test","user","password","test@user.com") 
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)

if __name__ == '__main__':
    unittest.main() 

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Password.password_list = []

def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = Password("Test","user","password","test@user.com") 
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)

if __name__ == '__main__':
    unittest.main()      

 
      