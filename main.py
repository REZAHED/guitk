from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('dictionary v.1.0')
root.geometry('800x600')



def on_closing():
    toplevel = Toplevel(root)

    toplevel.title("закрыть программу")
    toplevel.geometry(f"300x100+{root.winfo_x()+250}+{root.winfo_y()+200}")

    l1=Label(toplevel, image="::tk::icons::question")
    l1.grid(row=0, column=0, pady=(7, 0), padx=(10, 30), sticky="e")
    l2=Label(toplevel,text="вы действиетльно хотите выйти?")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
    b1 = Button(toplevel, text="Да", command=root.destroy, width=10)
    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2 = Button(toplevel, text="Нет", command=toplevel.destroy, width=10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")

root.protocol('WM_DELETE_WINDOW',on_closing)

root.mainloop()
