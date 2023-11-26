"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math
import webbrowser

def play_video(url):
    webbrowser.open(url)

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
    pi = (str(3.1415926535897932384))
    # TODO) Print out the first 3 digits of pi. For example,
    Lscore = 0
    score = 0
    for i in range(17):
        g = pi[i]
        q = simpledialog.askstring(None, prompt="what is the next digit of pi?")
        if q == g:
            print("correct")
            score = score + 1
        elif q == "shrek fart":
            play_video('https://www.youtube.com/watch?v=-WkIrqFbEb4')
        else:
            print("incorrect")
            Lscore = Lscore + 1

    messagebox.showinfo(None, message="You got "+(str(score))+" digits of pi correct and "+(str(Lscore))+" incorrect!")

    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi


        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
