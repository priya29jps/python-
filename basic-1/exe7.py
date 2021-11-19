#Write a Python program to accept a filename from the user and print the extension of that.

# Python str.rsplit(sep=None, maxsplit=-1) function:

# The function returns a list of the words of a given string using a separator as the delimiter string.

# If maxsplit is given, the list will have at most maxsplit+1 elements.
# If maxsplit is not specified or -1, then there is no limit on the number of splits.
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
# The sep argument may consist of multiple characters.
# Splitting an empty string with a specified separator returns [''].



filename = input("enter the filename")
f_exten = filename.split(".")
print("the extension of the file is :" + repr(f_exten[-1]))

fname= input("enter the fname")
f_e = fname.split(".")
print("the extention of fname is:"+ repr(f_e[-1]))

