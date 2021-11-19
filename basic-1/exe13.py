# Write a Python program to calculate number of days between two dates.

# Python datetime.date(year, month, day) :

# The function returns date object with same year, month and day. All arguments are required. Arguments may be integers, in the following ranges:

# MINYEAR <= year <= MAXYEAR
# 1 <= month <= 12
# 1 <= day <= number of days in the given month and year

from datetime import date
f_date = date(2013,7,4)
l_date = date(2015,4,11)
delta = l_date - f_date
print(delta.days)