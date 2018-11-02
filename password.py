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

       