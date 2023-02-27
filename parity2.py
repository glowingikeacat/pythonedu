def main():
    x = int(input("What's x? "))
    if y(x):
        print("Even")
    else:    
        print("Odd")

# This is the working function
def y(n):
    return True if n % 2 == 0 else False

main()