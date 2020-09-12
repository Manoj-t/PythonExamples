#Python provided several methods to check type of characters in a string

#isalnum() --> returns True if string contains any of alphanumeric charactes
#isalpha() --> returns True if string contains only alphabets
#isdigit() --> returns True if string contains only digits
#islower() --> returns True if all alphabet characters in string are lower case.
#isupper() --> returns True if all alphabets in string are upper case.
#istitle() --> returns True if string is Title case
#isspace() --> returns True if string contains only space.

print('python123'.isalnum()) #True
print('pythoniseasy'.isalpha())  #True
print('strings123'.isdigit()) #False
print('6754'.isdigit()) #True
print('Learning Python is very easy'.islower()) #False
print('learning is good'.islower()) #True
print('LEARNING IS GOOD'.isupper()) #True
print('Learning Python Is Easy'.istitle()) #True
print('learning  '.isspace()) #False
print('  '.isspace()) #True
