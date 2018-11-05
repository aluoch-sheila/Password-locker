#!/usr/bin/env python3.6
from password import Password

def create_password(fname,lname,password,email):
   '''
   Function to create a new password
   '''
   new_password = Password(fname,lname,email,password)
   return new_password

def save_password(password):
   '''
   Function to save password
   '''
   password.save_password()

def del_password(password):
   '''
   Function to delete a password
   '''
   password.delete_password()


def find_password(email):
   '''
   Function that finds a password by number and returns the password
   '''
   return Password.find_by_number(email)
def check_existing_password(email):
   '''
   Function that check if a password exists with that number and return a Boolean
   '''
   return Password.password_exist(email)
def display_password():
   '''
   Function that returns all the saved password
   '''
   return Password.display_passwords()




def main():
   print("Hello . What is your name?")
   user_name = input()

   print(f"Hi {user_name}. Do you want to proceed?")

   print('\n')

   while True:
       print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

       short_code = input().lower()

       if short_code == 'cc':
           print("New Account")
           print("-"*10)

           print ("Sir Name ....")
           f_name = input()

           print("Last name ...")
           l_name = input()

           print("Email ")
           email = input()

           print("Password")
           password = input()


           save_password(create_password(f_name,l_name,password,email))
           print ('\n')
           print(f"New Account {f_name} {l_name} {password} {email} created")
           print ('\n')

       elif short_code == 'dc':

           if display_password():
               print("Here are your account details")
               print('\n')

               for password in display_password():
                   print(f"{password.first_name} {password.last_name} .....{password.password} {password.email}")

               print('\n')
           else:
               print('\n')
               print("Your account is empty")
               print('\n')

       elif short_code == 'fc':

           print("Enter the name,email you want to search for")

           search_email = input()
           if check_existing_password(search_email):
               search_password = find_password(search_email)
               rint(f"{search_password.first_name} {search_password.last_name} {search_password.email} {search_password.password}")
               print('-' * 20)

               print(f"Password.......{search_password.email}")
               print(f"Email.....{search_password.email}")
           else:
               print("That Account does not exist")

       elif short_code == "ex":
           print("Thanks for your time .......")
           break
       else:
           print("The server. Please use the short codes")
if __name__ == '__main__':

   main()