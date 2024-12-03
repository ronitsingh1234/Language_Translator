from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from googletrans import Translator, LANGUAGES


# Translator function setup
def top():
    def change(text="type", src="English", dest="Hindi"):
        t1 = text
        s = src
        d = dest
        trans = Translator()
        trans1 = trans.translate(text, src=s, dest=d)
        return trans1.text

    def data():
        s = comboboxofsource.get()
        d = comboboxofdest.get()
        t = Source_text.get(1.0, END)
        textget = change(t, s, d)
        dest_text.delete(1.0, END)
        dest_text.insert(END, textget)

    root = Toplevel(win)
    root.title("Language Translator")
    root['bg'] = "black"
    root.geometry("1920x1080")
    root.iconbitmap(r"C:\Users\Ronit Singh\Downloads\googletranslate_translate_3280.ico")
    
    photo1 = PhotoImage(file=r"C:\Users\Ronit Singh\Downloads\pixelcut-export.png") 
    label01 = Label(root, image=photo1, relief="sunken")
    label01.place(x=0, y=0, width=1700, height=850)
    
    label = Label(root, text="", bg="light yellow", relief="sunken")
    label.place(x=303, y=49, width=989, height=560)
        
    lab_txt = Label(root, text="TRANSLATOR", font=("ARIAL BLACK", 20, "bold"), bg='khaki2', fg='black')
    lab_txt.place(x=680, y=55, height=40, width=210)

    list_text = list(LANGUAGES.values())
   
    comboboxofsource = ttk.Combobox(root, value=list_text)
    comboboxofsource.place(x=440, y=90, height=40, width=140)
    comboboxofsource.set("English")

    button = Button(root, text="TRANSLATE", font=("ARIAL", 10, "bold"), relief=RAISED, command=data)
    button.place(x=730, y=340, height=40, width=140)

    comboboxofdest = ttk.Combobox(root, value=list_text)
    comboboxofdest.place(x=1000, y=90, height=40, width=140)
    comboboxofdest.set("Hindi")
    
    lab_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "normal"), fg='black', bg='light yellow')
    lab_txt.place(x=430, y=170, height=30, width=150)

    Source_text = ScrolledText(root, font=("Times New Roman", 20, "normal"), bg='white', wrap=WORD)
    Source_text.place(x=320, y=220, height=350, width=370)

    d_txt = Label(root, text="Destination Text", font=("Times New Roman", 20, "normal"), fg='black', bg='light yellow')
    d_txt.place(x=990, y=170, height=30, width=200)

    dest_text = ScrolledText(root, font=("Times New Roman", 20, "normal"), bg='white', wrap=WORD)
    dest_text.place(x=910, y=220, height=350, width=370)

    root.mainloop()

# Chatbot setup
def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but thank you for asking!",
        "what is your name": "I'm your friendly chatbot.",
        "bye": "Goodbye! Have a nice day!"
    }
    user_input = user_input.lower()
    return responses.get(user_input, "I'm here to chat! Please tell me more.")

def window():
    def send_message():
        user_input = user_text.get(1.0, END).strip()
        if user_input:
            chatbox.insert(END, "You: " + user_input + "\n")
            response = chatbot_response(user_input)
            chatbox.insert(END, "Bot: " + response + "\n\n")
            user_text.delete(1.0, END)

    chat_win = Toplevel(win)
    chat_win.title("Tranzio")
    chat_win.geometry("500x600")
    chat_win.config(bg="lightblue")

    # Chat display area
    chatbox = ScrolledText(chat_win, font=("Arial", 14), wrap=WORD, bg="white")
    chatbox.place(x=20, y=20, width=460, height=450)
    chatbox.insert(END, "Bot: Hi! I'm here to chat with you. Type your message below.\n\n")

    # Input field for user message
    user_text = Text(chat_win, font=("Arial", 14), height=3, bg="white")
    user_text.place(x=20, y=500, width=360, height=50)

    # Send button
    send_button = Button(chat_win, text="Send", font=("Arial", 12), command=send_message)
    send_button.place(x=400, y=510, width=60, height=30)

# Main window setup
win = Tk()
win.geometry("1920x1080")
win["bg"] = "grey"
photo = PhotoImage(file=r"C:\Users\Ronit Singh\Downloads\ron.png")
label = Label(win, image=photo, bg="grey", relief="sunken")
label.place(x=0, y=0, height=850)

button = Button(win, text="TRANSLATOR", font=("Arial", 20, "bold"), command=top)
button.place(x=500, y=300, width=200)
button = Button(win, text="CHATBOT", font=("Arial", 20, "bold"), command=window)
button.place(x=750, y=300, width=200)

win.mainloop()
