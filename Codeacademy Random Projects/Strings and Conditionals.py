# Strings and Conditionals (Part Two)

# Question 1: 
# Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string. For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.

def contains(big_string, little_string):
  return little_string in big_string

# defining the variable 'contains' with two inputs and it is asking if input 1 is in input 2, it will return a boolean to indicate the answer

print(contains("watermelon", "melon"))
# prints out 'True' 

# Question 2:
# Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

def common_letters(string_one, string_two):
  list = []
  for letter in string_one:
    if(letter in string_two) and not (letter in list):
      list.append(letter)
  return list

# (1) first we define our variable with two inputs and also create an empty list (2) then we create the for loop (3) which has the conditional statement inside of it and says that if letter is in string_one (i.e. return a boolean) and if it's not in the list (which is empty, and will be filled as this goes through the loop...) then add it to the list (4) else return the list 

print(common_letters("manhattan", "san francisco"))
# returns back ['a','n']

#Introduction to Strings summary question

# 1.  
# Copeland’s Corporate Company has finalized what they want their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.
# Let’s start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a username. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.
# For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.

def username_generator(first_name, last_name): # create variable with 2 inputs
  if len(first_name) < 3:       # if the length of the first_name is less than 3 then...
    user = first_name           # the user = first_name
  else:                         # else
    user = first_name[0:3]      # the user = the first three letters in the first_name
  if len(last_name) < 4:        # if the length of the last_name is less than 4 then...
    user += last_name           # the user = last_name
  else:                         # else
    user += last_name[0:4]      # the user = the first four letters of the last_name
  return user                   # return the user ... i.e. the result of the conditional statements inside of the variable

print(username_generator("Abe", "Simpson"))
# returns 'AbeSimp'

