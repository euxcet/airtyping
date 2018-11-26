import tkinter as tk

class KeyboardView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Air Typing")
    def mainloop(self):
        self.window.mainloop()



class KeyboardController:
    def __init__(self):
        self.view = KeyboardView()

    def run(self):
        self.view.mainloop()
