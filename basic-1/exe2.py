#Write a Python program to display the current date and time


# from datetime import datetime
# current = datetime.current()
# print("todays date ",current)


# import datetime
# now = datetime.datetime.now()
# print("current date and time")
# print(now.strtime("%Y-%M-%D %H-%M-%S"))


#note:- date.strtime(format) returns a string representing the date,controlled by an explicit format string. format codes referring to hours ,minutwa or second will bwe zero
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

