# Python: String Slicing

# Write a function called password_generator() that takes two inputs, first_name and last_name, and then concatenates the last three letters of each and returns them as a string.


first_name = "Reiko"
last_name = "Matsuki"

# function with two inputs, taking the last characters from each
def password_generator(first_name, last_name):
  temp = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp

# testing function, saving it to the variable temp_password
temp_password = password_generator(first_name, last_name)

print(temp_password)
#prints out ----> ikouki

