'''
 Suppose you need to write a program to take a survey of university
students' extra curriculum activities. Now you can use IF ELSE statement to do
this:
->If a user inputs “brilliant” then show “The Student is more active and sincere”.
->If a user inputs “better” then show “The Student is trying to join extra curriculum
activities”.
->If a user inputs “good” then shows “The Student is learn about extra curriculum
activities”.
->If a user inputs “Nothing” then show “The Student does not join any extra
curriculum activities Yet”.

'''

user_input=input("user input : ")
if 'briliant' in user_input:
  print('The Student is more active and sincere')
elif 'better' in user_input:
  print('The Student is trying to join extra curriculum activities')
elif 'good' in user_input:
  print('The Student is learn about extra curriculum activities')
elif 'nothing' in user_input:
  print('The Student does not join any extra curriculum activities Yet')