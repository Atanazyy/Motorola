import tkinter
import convert

root = tkinter.Tk()
root.geometry('480x480')

title = tkinter.Label(root, text='Bioinformatyka')

title.pack()

e = tkinter.Entry(root, borderwidth = 5)
e.pack(side=tkinter.LEFT)

def rozkod():
    RNA = e.get().replace(" ", "")
    amino = tkinter.Label(root, text = RNA)
    amino.pack()
    proteins = convert.decode(RNA)
    if (type(proteins) is int):
        print("Blad numer", proteins)
        return proteins
    print(proteins)

s = tkinter.Button(root, text = 'Submit', command = rozkod)
s.pack(side=tkinter.BOTTOM)

root.mainloop()
