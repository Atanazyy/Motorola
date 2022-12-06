import tkinter
import convert

root = tkinter.Tk()
root.geometry('480x480')

title = tkinter.Label(root, text='Bioinformatyka')

title.pack()

e = tkinter.Entry(root, borderwidth = 5)
e.pack(side = tkinter.LEFT)

def rozkod():
    RNA = e.get().replace(" ", "")

    proteins = convert.decode(RNA)
    proteins = tkinter.Label(root, text=proteins)
    proteins.pack()

s = tkinter.Button(root, text = 'Submit', command = rozkod)
s.pack(side = tkinter.BOTTOM)

root.mainloop()
