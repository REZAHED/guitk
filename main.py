import os
import sys
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox

import psutil as psutil
import tendo
from tendo import singleton
root = Tk()
root.title('dictionary v.1.0')
root.geometry('800x600')
root.columnconfigure(9)
root.rowconfigure(9)
f=open('run.dll','w+')
f.close()
def delet_file():
    if os.path.exists('run.dll'):
        print('yes')
        os.remove('run.dll')

def on_closing():
    toplevel = Toplevel(root)

    toplevel.title("закрыть программу")
    toplevel.geometry(f"300x100+{root.winfo_x()+250}+{root.winfo_y()+200}")

    l1=Label(toplevel, image="::tk::icons::warning")
    l1.grid(row=0, column=0, pady=(0, 7), padx=(10, 30), sticky="e")
    l2=Label(toplevel,text="вы действиетльно хотите выйти?")
    l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
    b1 = Button(toplevel, text="Да", command=lambda :[delet_file(),root.destroy()], width=10)

    b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
    b2 = Button(toplevel, text="Нет", command=toplevel.destroy, width=10)
    b2.grid(row=1, column=2, padx=(2, 35), sticky="e")

    toplevel.grab_set()

root.protocol('WM_DELETE_WINDOW',on_closing)




lbl_input=Label(root,text="введите слово для поиска:",font=('muller',12))
lbl_input.place(x=10,y=4)
text_box_input=Text(root,width=25, height=1,selectbackground="blue",borderwidth=2)
text_box_input.place(x=10,y=35)
text_box_input.config(font=('muller',20,'bold'))

lbl_output=Label(root,text="перевод:",font=('muller',12))
lbl_output.place(x=10,y=80)
text_box_output=Text(root,width=25, height=1,selectbackground="blue",borderwidth=2)
text_box_output.place(x=10,y=120)
text_box_output.config(font=('muller',20,'bold'),state='disabled')

btn = Button(root, text="поиск")
btn.place(x=400,y=80)

# procs = [p for p in psutil.process_iter() if 'main.exe' in p.name()]
#
# if len(procs) > 2:
#     root.withdraw()
#     messagebox.showerror("ошибка",'у вас уже открыто приложение!')
#
#     root.destroy()
# else:
if os.path.exists('run.dll') and os.path.getsize('run.dll')==0:
    f = open('run.dll', 'r+')
    f.write("0")
    f.close()
    root.mainloop()






# try:
#     me = singleton.SingleInstance()
# except tendo.singleton.SingleInstanceException:
#
#
#
#        root.withdraw()
#        messagebox.showerror("ошибка",'у вас уже открыто приложение!')
#
#     # t = Toplevel(root)
#     # t.title("закрыть программу")
#     # t.geometry(f"300x100+{root.winfo_x() + 250}+{root.winfo_y() + 200}")
#     #
#     # l1 = Label(t, image="::tk::icons::warning")
#     # l1.grid(row=0, column=0, pady=(0, 7), padx=(10, 30), sticky="e")
#     # l2 = Label(t, text="У вас уже открыто приложение")
#     # l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
#     # b1 = Button(t, text="Да", command=lambda :[root.destroy(),t.destroy()],  width=10)
#     # b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
#
#        root.destroy()





# else:


