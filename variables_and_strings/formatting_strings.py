#Formatting strings

# like the template literal sof JavaScript

x = 10

formatted = f"I've tolf you {x} times already!"
print(formatted)

hello = f"Hello there {x} times!"
print(hello)

# python2 way of formatting strings
hello = "Hello there {} times!".format(10)
print(hello)

first = "Dimitri"
last = "Nakos"

formatted = "First Name: {}, Last Name: {}".format(first, last)
print(formatted)


#index
print(formatted[4])