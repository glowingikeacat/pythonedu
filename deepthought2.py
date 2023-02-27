# this is the program where I learned how to use the case (match)
answer = input("What's the secret of the Universe? ")

match answer:
    case "forty-two":
        print("Yes, that's correct but remove the hyphen, I don't like hyphens")
    case "forty two":
        print("Yes, thats' correct but use a number, it's more efficient that risking carpal tunnel syndrome--honestly...")
    case "42":
        print("Yes, this the correct answer." )
    case other:
        print("No, incorrect... try again.  ")