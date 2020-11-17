#importing modules
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import os
#global variable 
global file

#main window
np=Tk()

#functions
def copy():
	t.event_generate(("<<Copy>>"))

def cut():
	t.event_generate(("<<Cut>>"))

def paste():
	t.event_generate(("<<Paste>>"))

def delete():
	t.delete(0.0,END)

def exit():
	np.destroy()

def undo():
	t.edit_undo()

def select_all():
	t.event_generate('<<SelectAll>>')

def about_np():
	messagebox.showinfo('About','made by ankita0606')

def new_file():
	file=None
	t.delete(1.0,END)
	np.title("Untitled-Notepad")

def save_file():
	
	file=asksaveasfilename(defaultextension=".txt",filetypes=[("text file","*.txt*"),("all documents","*.*")])
	f=open(file,'w')
	f.write(t.get(0.0,END))
	f.close()
	print('saved')
	np.title(os.path.basename(file)+"-Notepad")


def open_file():
    
    fi=askopenfilename(parent=np,defaultextension=".txt",filetypes=[("text file","*.txt*"),("all documents","*.*")])
    try:
    	fe=open(fi,'r')
    	if fi==" ":
    		file==None
    	else:
    		fe=open(fi,'r')
    		np.title(os.path.basename(fi)+"-Notepad")
    		t.delete(1.0,END)
    		t.insert(1.0,fe.read())
    		fe.close()
    except:
    	messagebox.showinfo("Information","file do not exit")


#textarea

t=Text(np,height=50,width=200)
#scrollbar
yscrollbar=Scrollbar(t)
xscrollbar=Scrollbar(t,orient="horizontal")
xscrollbar.pack(side=BOTTOM,fill=X)
xscrollbar.config(command=t.xview)
yscrollbar.pack(side=RIGHT,fill=Y)
yscrollbar.config(command=t.yview)
#np.iconbitmap(r"C:\Users\hp\Desktop\notepad icon pic")
t.config(yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set)
file=None
t.pack(expand=True,fill=BOTH)
t.focus()
np.title("Untitled-Notepad")

# making menu
menu=Menu(np)
menu1=Menu(menu,tearoff=0)

menu1.add_command(label="New", accelerator="Ctrl+N",command=new_file)
menu1.add_command(label="Open...",accelerator="Ctrl+O",command=open_file)
menu1.add_command(label="Save...",accelerator="Ctrl+S",command=save_file)
menu1.add_separator()

menu1.add_command(label="Exit",command=exit)
menu.add_cascade(label="File",menu=menu1)

menu2=Menu(menu,tearoff=0)
menu2.add_command(label="undo",command=undo,accelerator="Ctrl+Z")
menu2.add_separator()
menu2.add_command(label="Cut",command=cut,accelerator="Ctrl+X")
menu2.add_command(label="Copy",command=copy,accelerator="Ctrl+C")
menu2.add_command(label="Paste",command=paste,accelerator="Ctrl+V")
menu2.add_command(label="Delete",command=delete,accelerator="Del")
menu.add_cascade(label="Edit",menu=menu2)

menu3=Menu(menu,tearoff=0)
menu3.add_command(label="About Notepad",command=about_np)
menu.add_cascade(label="Help",menu=menu3)
np.config(menu=menu)

np.mainloop()