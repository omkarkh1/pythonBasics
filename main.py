message = "heLlo world"

print(message)

print(message.title())

print(message.upper())

print(message.lower())

message = f"say {message}"

print(message)

print("\ttabbed")

print("First line\nSecond line")

message = "1\ttab\t2"

"""
The reason there is more space between "1" and "tab" than between "tab" and "2" in the output of your code lies in how the tab character (\t) works. A tab does not represent a fixed number of spaces but instead moves the cursor to the next tab stop, which is typically set at fixed intervals (e.g., every 8 characters). The spacing depends on the position of the cursor when the tab is encountered.
"""

print(message)
print(message.strip())
print(message.lstrip())
print(message.rstrip())

url = 'https://google.com'
url.removeprefix('https://')

print(url)

value = 10_0_0_1010
print(value)


## The zen of python

import this


# Inserting element in the list
#
# (append and insert)

value = ["NY","California","Texas"]

print(value)

value.insert(0,"London")

print(value)

del value[0]

print(value)

value.remove("NY")

print(value)

value.pop(0) #-1 be default

print(value)

# index error - out of index

# Many Python programmers recommend that each line should be less than
# 80 characters. Historically, this guideline developed because most computers could fit only 79 characters on a single line in a terminal window.
# Currently, people can fit much longer lines on their screens, but other reasons exist to adhere to the 79-character standard line length.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


class Car:
 def __init__(self):
  self.a = 0
  print("car")


class BMW(Car):
 def __init__(self):
  super().__init__()
  print("bmw")

bmw = BMW()

#aliases

import math as mat
print(mat.ceil(4.00001))

from random import randint,choice

from pathlib import Path
path = Path("pi_digits.txt")
print(path.read_text())

print(type(path.read_text()))

contents = path.read_text()
for content in contents.splitlines():
 print(content)

# path = Path('pi_digits.txt')
# path.write_text("I love programming.")
# print("---------------------------")
# contents = path.read_text()
# print(contents)

# FileNotFoundError Exception


