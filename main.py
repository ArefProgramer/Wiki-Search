#Library
from tkinter import filedialog as windowfile,messagebox as tkmsg
from tkinter import *
import tkinter as tk
from customtkinter import *
import wikipedia as wiki
from customtkinter import CTkFont
from CTkMessagebox import *
from CTkMenuBar import *
import pyperclip
#data program
lan = ""
type_text = ""
#Program
name = "Wiki Search"
version = "2.0.0"
dev = "Aref Sadegh"
#config window
win  = CTk()
win.iconbitmap("i.dll")
win.title(name)
win.geometry("555x350")
win.resizable(False,False)
def exit_program():
     askmsg =   tkmsg.askyesno(name +" - Exit","Do you want to Exit?")
     if(askmsg==1):
           win.destroy()
def about():
      CTkMessagebox(title= name+ " - About", icon="ia.dll",message=f"{name} Version {version} Copyright © 2025\nDeveloper {dev}")
def copy():
     pyperclip.copy(textbox.get(1.0,"end-1c"))
def savefile():
     file = windowfile.asksaveasfilename(title=name + " - Save File",defaultextension="*.txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
     if(file==""):
          return
     else:
          with open(file,"w",encoding='utf-8') as write_file:
            write_file.write(textbox.get(1.0,"end-1c"))
def search_work():
    if(text_language.get()=="" or text_subject.get() =="" or text_typetext.get()==""):
        tkmsg.showerror(name + " - Error","Fill in all the fields")
    else:
        global lan,type_text
        if(text_language.get()=="English"):
              
              lan="en"
        elif(text_language.get()=="عربی"):
             
              lan="ar"
        else:
             lan="fa"
        #selct type o text
        if(text_typetext.get()=="Normal"):
            type_text="n"
        elif(text_typetext.get()=="Summary"):
             type_text="s"
        else:
    
            dialog = CTkInputDialog(text="Enter the desired number of lines", title=name +" - Select the number of summarized lines")
      
            image = tk.PhotoImage(file="ia.dll")
            dialog.after(250, dialog.iconphoto, False, image)
            
                
            type_text=int(dialog.get_input())
        wiki.set_lang(lan)
        if(type_text=="n"):
            textbox.delete(0.0,"end-1c")
            page = wiki.page(text_subject.get())
            text_wiki_output = page.content
            textbox.insert("end-1c",text_wiki_output)
        elif(type_text=="s"):
             textbox.delete(0.0,"end-1c")
             page = wiki.summary(text_subject.get(),sentences=5)
             text_wiki_output=page
             textbox.insert("end-1c",text_wiki_output)
        else:
             textbox.delete(0.0,"end-1c")
             page = wiki.summary(text_subject.get(),sentences=type_text)
             text_wiki_output=page
             textbox.insert("end-1c",text_wiki_output)
             


      
             
#labels
label_subject = CTkLabel(win,text="Subject")

label_subject.pack()
label_subject.place(x=0,y=40)

label_language = CTkLabel(win,text="Language")
label_language.pack()
label_language.place(x=0,y=80)

label_typetext = CTkLabel(win,text="Type of Text")
label_typetext.pack()
label_typetext.place(x=0,y=120)


text_subject = CTkEntry(win,font=CTkFont(family="Calibri"))
text_subject.pack()
text_subject.place(x=90,y=40)

text_language = CTkComboBox(win,font=CTkFont(family="Calibri"),values=['English','فارسی','عربی'])
text_language.pack()
text_language.place(x=90,y=80)



text_typetext = CTkComboBox(win,font=CTkFont(family="Calibri"),values=['Normal','Summary','Select the number of summarized lines'])
text_typetext.pack()
text_typetext.place(x=90,y=120)

textbox = CTkTextbox(win,font=CTkFont(family="Calibri",size=12),height=310,width=300)
textbox.pack()
textbox.place(x=252,y=40)

#Button
button_search = CTkButton(win,text="Search",width=250,command=search_work)
button_search.pack()
button_search.place(x=0,y=160) 


win_menu = CTkMenuBar(win)
win_menu.add_cascade(text="Exit",command=exit_program)
win_menu.add_cascade(text="About",command=about)
#right click

right_menu = Menu(textbox, tearoff = 0) 


right_menu.add_command(label ="Copy",command=copy) 
right_menu.add_command(label ="Save File",command=savefile) 
#config right click
def do_popup(event): 
    try: 
        right_menu.tk_popup(event.x_root, event.y_root) 
    finally: 
        right_menu.grab_release() 
textbox.bind("<Button-3>", do_popup) #Click  right work at textbox




#Textbox
win.mainloop()









