# Python Docstring:

# A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object.

# All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings.

import calendar
y = int(input("enter the year"))
m = int(input("enter thr month"))
print(calendar.month(y,m))



# import calendar
year = int(input("enter the year"))
month = int(input("enter the month"))
print(calendar.month(year,month))