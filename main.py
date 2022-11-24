import sys
import time
import os
# os.environ["OMP_NUM_THREADS"]= '4'
# os.environ["OMP_THREAD_LIMIT"] = '4'
# os.environ["MKL_NUM_THREADS"] = '4'
# os.environ["NUMEXPR_NUM_THREADS"] = '4'
# os.environ["OMP_NUM_THREADS"] = '4'
# os.environ["PAPERLESS_AVX2_AVAILABLE"]="True"
# os.environ["OCR_THREADS"] = '4'
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.messagebox import showinfo

# if hasattr(sys, "set_int_max_str_digits"):
#     sys.set_int_max_str_digits(1001000)
#
#
#
# print(5**1000000)
import psutil as psutil
import tendo
from tendo import singleton
from tqdm import tk

import openfile

# os.environ["MKL_NUM_THREADS"] = "1"
root = Tk()
root.title('dictionary v.1.0')
root.resizable(False,False)
root.geometry('800x600')


root.columnconfigure(0,weight=2)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.columnconfigure(4,weight=1)

root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)
root.rowconfigure(5,weight=4)
root.rowconfigure(6,weight=1)


def logging(text):

    current = time.strftime("%Y-%m-%d %H:%M:%S")
    log = open('log.txt', 'a+')
    log.write(str('>>>') + ' - ' + text + " " + current + '\n')
    log.close()



if not os.path.exists('log.txt'):
    log = open('log.txt', 'w+')
    log.close()

if os.path.exists('run.dll') and os.path.getsize('run.dll') == 0:

    f = open('run.dll', 'a+')
    f.write("Error 0000000 - try to open program when it's running")
    f.close()
    logging("Error 0000000 - try to open program when it's running")

    root.withdraw()

    messagebox.showerror("ошибка", 'у вас уже открыто приложение!')

    if os.path.exists('run.dll'):
        f = open('run.dll', 'w+')
        f.write("")
        f.close()
    root.destroy()
elif os.path.exists('run.dll') and os.path.getsize('run.dll') > 0:
    logging("Error 0000000 - try to open program when it's running")
    root.destroy()
else:
    f = open('run.dll', 'w+')
    f.close()


    def delet_file():
        if os.path.exists('run.dll'):
            print('yes')
            f.close()
            os.remove('run.dll')
#######################################################
    ########################################################
    def search():
        text_box_output.config(state='normal')
        text = text_box_input.get(0.0,END).strip().lower()
        read = openfile.OpenFile()
        dic_ = read.opening_json('dictionary.json')
        if dic_ is not None and text in dic_.keys():

            text_box_output.delete('1.0', END)
            text_box_output.insert('0.0',dic_[text])
            text_box_output.config(state='disabled')
        elif dic_ is not None and text in dic_.values():
            reverse_dic= {v: k for k, v in dic_.items()}
            text_box_output.delete('1.0', END)
            text_box_output.insert('0.0', reverse_dic[text])
        else:
            text_box_output.delete('1.0', END)
            text_box_output.insert('0.0', 'такого слово не найдено')
            text_box_output.config(state='disabled')




    #######################################################
    ########################################################
    def on_closing():
        toplevel = Toplevel(root)

        toplevel.title("закрыть программу")
        toplevel.geometry(f"300x100+{root.winfo_x() + 250}+{root.winfo_y() + 200}")

        l1 = Label(toplevel, image="::tk::icons::warning")
        l1.grid(row=0, column=0, pady=(0, 7), padx=(10, 30), sticky="e")
        l2 = Label(toplevel, text="вы действиетльно хотите выйти?")
        l2.grid(row=0, column=1, columnspan=3, pady=(7, 10), sticky="w")
        b1 = Button(toplevel, text="Да", command=lambda: [delet_file(), root.destroy()], width=10)

        b1.grid(row=1, column=1, padx=(2, 35), sticky="e")
        b2 = Button(toplevel, text="Нет", command=toplevel.destroy, width=10)
        b2.grid(row=1, column=2, padx=(2, 35), sticky="e")

        toplevel.grab_set()


    root.protocol('WM_DELETE_WINDOW', on_closing)

    lbl_input = Label(root, text="введите слово для поиска:", font=('muller', 12))
    lbl_input.grid(column=0,row=0,sticky='w',padx=20,pady=5)
    text_box_input = Text(root, width=25, height=1, selectbackground="blue", borderwidth=2)
    text_box_input.grid(row=1, column=0,sticky='w',padx=20)
    text_box_input.config(font=('muller', 20, 'bold'))

    lbl_output = Label(root, text="перевод:", font=('muller', 12))
    lbl_output.grid(column=0,row=2,sticky='w',padx=20)
    text_box_output = Text(root, width=25, height=1, selectbackground="blue", borderwidth=2)
    text_box_output.grid(row=3, column=0,sticky='w',padx=20)
    text_box_output.config(font=('muller', 20, 'bold'),state='disabled')

    btn = Button(root, text="    поиск    ",command=search)
    btn.grid(column=0,row=2, sticky='e')

    btn_save = Button(root, text="сохранить", command=search)
    btn_save.grid(column=0,row=1, sticky='e')

    #######################################################
    ########################################################
    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))
    columns = ('Слово', 'Перевод')
    tree = ttk.Treeview(root, columns=columns, show='headings')

    # define headings
    tree.heading('Слово', text='Слово')
    tree.heading('Перевод', text='Перевод')
    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=5, column=0, sticky='nsew',padx=20,columnspan=5)
    scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=5, column=5, sticky='ns')
    # procs = [p for p in psutil.process_iter() if 'main.exe' in p.name()]
    #
    # if len(procs) > 2:
    #     root.withdraw()
    #     messagebox.showerror("ошибка",'у вас уже открыто приложение!')
    #
    #     root.destroy()
    # else:
    # if os.path.exists('run.dll') and os.path.getsize('run.dll')==0:
    #     f = open('run.dll', 'r+')
    #     f.write("0")

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
