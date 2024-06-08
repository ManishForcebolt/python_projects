from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# from translate import Translator
# translator = Translator(to_lang="zh")
# translation = translator.translate("I have a pen.")


# tkinter GUI window named root
root = Tk()
root.geometry('700x320')
root.resizable(0, 0)
root.iconbitmap("icon3.png")
root['bg'] = 'green'

# Header Text of window
root.title('Language Translator - Python')
Label(root, text="Language Translator", font="Times 20 bold").pack()

# Inside body Label
Label(root, text="Enter Text", font="Times 13 bold").place(x=30, y=90)
# Inside body Input Text Entry box
Input_text = Entry(root, width=30)
Input_text.place(x=30, y=130)
Input_text.get()
# Inside body Output Text Box
Label(root, text="Output", font="Times 13 bold").place(x=380, y=90)
output_text = Text(root, font="Times 13 bold", height=10, width=40, wrap=WORD, padx=5, pady=5)
output_text.place(x=380, y=120)

# Language menu
language = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=language, width=20)
dest_lang.place(x=30, y=165)
dest_lang.set('Choose Language')


# Function to change the language
def translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)


trans_btn = Button(root, text='Translate', font="Times 13 bold", pady=5, command=translate,
                   bg="yellow", activebackground='red')
trans_btn.place(x=30, y=195)
root.mainloop()
