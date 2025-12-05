# A function that sorts S, the argument and prints it
def sorter(s):
    # A function that says how to sort in what order
    def sort_key(char):
        # first sort if any char in s is lower
        if char.islower():
            # will return 0 because its our first praiority
            return (0, char)
        elif char.isupper():
            return (1, char)
        elif char.isdigit():
            # if the char in s is a digit, convert it into a digit
            char = int(char)
            # checks if the number is odd
            if char % 2 != 0:
                return (2, char)
            # checks if the number is even
            else:
                return (3, char)
        # Checks for any other symbols like ,.: etc
        else:
            return (4, char)
    # join and prints what each returned using sorted function and key, it passes each character in s as argument in the sort_key()
    print("".join(sorted(s, key=sort_key)))
# Asks user to input the alphaneumetric they want to sort
sorter(input("Enter the sentence of alphaneumetric you want to arrange: "))