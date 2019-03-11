import tkinter


import Core


class Block:
    def __init__(self, master):
        self.e = tkinter.Entry(master, width=22)
        self.b = tkinter.Button(master, text="  Ask  ")
        self.l = tkinter.Label(master, bg='black', fg='white', width=26)

        self.b['command'] = self.processing

        self.e.pack()
        self.b.pack()
        self.l.pack()

    def processing(self):
        s = self.e.get()
        self.e.delete(0, 'end')

        answer, result, error = Core.main(s)

        if error == 0 and result == True:
            self.l['text'] = ' '.join(str(answer))
        elif error != 0:
            self.l['text'] = ' '.join(str(error))
        elif not result:
            self.l['text'] = ' '.join("Sorry, I can't help you")


def main():

    #  GUI initialise
    root = tkinter.Tk()

    #  right-bottom side of the screen
    root.geometry('200x80+1040+540')

    #  creating main window
    main_window = Block(root)

    root.mainloop()
