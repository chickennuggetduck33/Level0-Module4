"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi = (str(3.1415926535897932384))
    # TODO) Print out the first 3 digits of pi. For example,
    print(pi[0])
    print(pi[1])
    print(pi[2])
    print(pi[3])

    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi
    while True:
        simpledialog.askinteger(None, prompt="what is the next digit of pi?")
        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
