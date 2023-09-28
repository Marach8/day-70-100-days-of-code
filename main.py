import os

print('⭐Login Page⭐')
print ()
admin1 = os.environ['admin1']
pass1 = os.environ['pass1']
user1 = os.environ['user1']
pass2 = os.environ['pass2']


username = input('Enter your username: ')
password = input('Enter your password: ') 

print()
if username == admin1 and password == pass1:
  print('Welcome Admin')

elif username == user1 and password == pass2:
  print ('Welcome dear User')

else:
  print ('invalid login details!')