
# -*- coding: utf-8 -*-

import tkinter as tk

class AskBoxM(tk.Toplevel):

    def __init__(self,master,bg,qt,var, btns=['Yes','No']):
        self.master = master
        self.var = var
        #self.tl = tk.Toplevel.__init__(self, self.master, bg=bg, padx=1, pady=1)  # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.master, bg=bg, padx=1, pady=1)  # Initalise the Toplevel
        self.resizable(False, False)
        self.qtxt = tk.Text(self, fg='black',height=3, padx=2)
        self.qtxt.insert(tk.INSERT,qt)
        self.qtxt.configure(state=tk.DISABLED)
        self.qtxt.pack_propagate(False)
        self.qtxt.pack(side=tk.TOP,fill=tk.X)
        self.buframe = tk.LabelFrame(self,text='')
        for btn in btns :
            bu = tk.Button(self.buframe,text=btn)
            bu.bind('<Button-1>', self.btn_func)
            bu.pack(side=tk.LEFT)
        self.buframe.pack(side=tk.TOP)
        self.transient(self.master)
        self.grab_set()
        self.focus_set()
        #self.wait_window()

    def btn_func(self,event):
        btn = event.widget
        #print(btn['text'])
        self.var.set(btn['text'])
        self.destroy()

def get_askbox_result(var,qtext,butt):
    AskBox = AskBoxM(master=root, bg='blue', qt=qtext, var=var, btns=butt)
    AskBox.geometry('350x80+150+100')
    #AskBox.resizable(False, False)
    AskBox.wait_window()
    r = var.get()
    return r


if __name__ == '__main__':

    mainW = 800
    mainH = 300
    smX = 100
    smY = 30
    main_geo = ('{}x{}+{}+{}'.format(mainW, mainH,smX,smY))

    root = tk.Tk()
    root.geometry(main_geo)
    root.title('AskBoxM Testing')
    SomeVar = tk.StringVar()

    def ask():
        global SomeVar
        qt = qText.get('1.0',tk.END)
        r = get_askbox_result(SomeVar,qt,['Yes','Cancel'])
        print('r=',r)

    qText = tk.Text(root,  fg='black', height=6)
    qText.insert(tk.INSERT, 'Удалить указанный файл ?')
    qText.pack_propagate(False)
    qText.pack(side=tk.TOP, fill=tk.X)
    bu = tk.Button(root,text='Ask',command=ask).pack()

    root.mainloop()



