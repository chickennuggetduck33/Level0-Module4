"""
Use boolean variables to control program logic between two different code
paths.
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    day = simpledialog.askstring(title=None, prompt="is it the weekend?")
    isweekend = day == 'yes'
    if isweekend:
        print("yay the weekend")
    else:
        print("noooooooooo")
        pass
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    exam = simpledialog.askstring(title=None, prompt="did you pass the exam?")
    passexam = exam == 'yes'
    if passexam:
        print("yay good job")
    else:
        print("noooooooooo")
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.

    pass
