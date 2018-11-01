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
        self.new_password = Password("Sheila","Odongo","0711821055","aluochsheila1999@gmail.com") # create contact object


#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''

#         self.assertEqual(self.new_contact.first_name,"James")
#         self.assertEqual(self.new_contact.last_name,"Muriuki")
#         self.assertEqual(self.new_contact.phone_number,"0712345678")
#         self.assertEqual(self.new_contact.email,"james@ms.com")


# if __name__ == '__main__':
#     unittest.main()    