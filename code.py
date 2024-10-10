from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text = "type",src = "English",dest = "Hindi"):
    t1 = text
    s = src
    d = dest
    trans = Translator()
    trans1 = trans.translate(text ,src = s,dest = d)
    return trans1.text

def data():
    s = comboboxofsource.get()
    d = comboboxofdest.get()
    t = Source_text.get(1.0 , END)
    textget = change(t,s,d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)
    

root = Tk()
root.title("Google_Translator")
root.geometry("500x600")
root.config(bg ='silver')

lab_txt = Label(root,text = "Translator",font=("Times New Roman",20,"bold"),bg = 'black' ,fg = 'white')
lab_txt.place(x=150,y=30,height=40,width=200)

frame = Frame(root).pack(side = BOTTOM)

lab_txt = Label(root,text = "Source Text",font=("Times New Roman",20,"normal"),fg = 'black',bg = 'silver')
lab_txt.place(x=175,y=90,height=30,width=150)

Source_text = Text(frame,font=("Times New Roman",10,"normal"),bg = 'light blue',wrap = WORD)
Source_text.place(x=10,y=140,height=100,width=480)

list_text = list(LANGUAGES.values())

comboboxofsource = ttk.Combobox(frame,value = list_text)
comboboxofsource.place(x=10,y=260,height=40,width=140)
comboboxofsource.set("english")


button = Button(frame, text = "Translate",relief = RAISED,command = data)
button.place(x=180,y=260,height=40,width=140)


comboboxofdest = ttk.Combobox(frame,value = list_text)
comboboxofdest.place(x=350,y=260,height=40,width=140)
comboboxofdest.set("hindi")

d_txt = Label(root,text = "Destination Text",font=("Times New Roman",20,"normal"),fg = 'black',bg = 'silver')
d_txt.place(x=150,y=320,height=30,width=200)

 
dest_text = Text(frame,font=("Times New Roman",10,"normal"),bg = 'light blue',wrap = WORD)
dest_text.place(x=10,y=370,height=100,width=480)

root.mainloop()

