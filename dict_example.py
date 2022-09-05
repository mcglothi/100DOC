programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "A piece of code that repeats itself over and over again.",
}

# Retrieve a value from the dictionary
print(programming_dictionary["Bug"])

# Add a new key-value pair to the dictionary
programming_dictionary["Variable"] = "A variable is a named storage location for a value."

# Create empty dictionary
empty_dictionary = {}

# Edit a value in the dictionary
programming_dictionary["Bug"] = "A bug is an error in a program that prevents the program from running as expected."

# loop through the dictionary and print each key-value pair
for key, value in programming_dictionary.items():
  print(f"{key}: {value}")

# loop through the dictionary and print each key
for key in programming_dictionary.keys():
  print(key)

# loop through the dictionary and print each value
for value in programming_dictionary.values():
  print(value)

