# this simply program illustrates number systems from Python

# set up variables
x = float(input("What's X? "))
y = float(input("What's Y? "))

# round it down to three decimal places and print the results
z = round(x / y, 2)

#the f formats the answer and adds a comma every three digits
#print(f"{z:,}")

print (z)