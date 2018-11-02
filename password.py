class Password:
	"""
	Class that generates new instances of Password.
	"""
	password_list = []

	def __init__(self, first_name, last_name, password, email):
		self.first_name = first_name
		self.last_name = last_name
		self.password = password
		self.email = email

	
	def save_password(self):
		"""
		save_password method saves password objects into password_list
		"""
		Password.password_list.append(self)

	    # def test_delete_password(self):

	def delete_password(self):
		'''
		delete_password method deletes a saved password from the password_list
		'''

		Password.password_list.remove(self) 
	@classmethod
	def find_by_email(cls,email):
			'''
			Method that takes in a string and returns a password that matches that string.

			Args:
				password: password to search for
			Returns :
				Password of person that matches the sting.
			'''

			for password in cls.password_list:
				if password.email == email:
					return password			
				
		