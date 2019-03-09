import tkinter


root = tkinter.Tk()

e = tkinter.Entry(root, width=20)
b = tkinter.Button(root, text="Ask")
l = tkinter.Label(root, bg='black', fg='white', width=20)


def processing(event):
    s = e.get()
    l['text'] = ' '.join(s)


b.bind('<Button-1>', processing)

e.pack()
b.pack()
l.pack()


def main():

    root.mainloop()
