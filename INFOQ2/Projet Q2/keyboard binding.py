from tkinter import *

window = Tk()
window.geometry("600x400")
window.title("Test")

def test(event):
    print("Hi")

window.bind("a", test)

window.mainloop()

screen = turtle.Screen()
def blabla():
    print("pute")
    # your code here
screen.listen()
screen.onkey(blabla, "b")