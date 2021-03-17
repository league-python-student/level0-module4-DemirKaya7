"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string.
    #  3.1415926535897932384
    pi_str = "3.1415926535897932384"

    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit
    print(pi_str[0])
    print(pi_str[1])
    print(pi_str[2])

    # TODO) Use a while loop to keep asking for the next digit of pi
    i = 3
    digit = simpledialog.askinteger(title="Digit", prompt="Enter the next digit of pi")
    while str(digit) == pi_str[i] and i < len(pi_str) - 1:
        print(str(digit) + " is correct")
        digit = simpledialog.askinteger(title="Digit", prompt="Enter the next digit of pi")
        i += 1

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop
    if(str(digit) == pi_str[i]):
        print("ALL CORRECT")
    else:
        print("Incorrect")


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
    print("You were able to recite " + str(i - 3) + " more digits of pi!")
