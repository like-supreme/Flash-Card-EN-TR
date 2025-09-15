#-----------------------IMPORTS---------------#
import pandas as pd
from tkinter import *
import random
import time as t
#--------------------CONSTANTS--------------#
BACKGROUND_COLOR = "#B1DDC6"
LITTLE_FONT = ("Ariel" , 40 , "italic")
BIG_FONT = ("Ariel" , 50 , "bold")
FOREGROUND_COLOR = "#0099cc"
#--------------STATES--------------------#
random_word = None
flip_timer = None
#--------------- Reading File---------------#
lang_file = pd.read_csv("C:/Users/mdeha/OneDrive/Masaüstü/python/day31/flash_card_project/data/turkish_words.csv")
words = lang_file.to_dict(orient="records")
#--------------Functions----------------------#
def next_card():
    global random_word , flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)   
    random_word = random.choice(words)
    english_word = random_word["English"]   
    canvas.itemconfig(card_fg, image=card_front)
    canvas.itemconfig(lang_text , text="English" , fill="black")
    canvas.itemconfig(word_text , text=english_word , fill="black")
 
    flip_timer = window.after(2500 , flip_card)
def flip_card():   
    turkish_word = random_word["Turkish"]

    canvas.itemconfig(card_fg , image=card_back)
    canvas.itemconfig(lang_text , text="Turkish" , fill="white")
    canvas.itemconfig(word_text , text= turkish_word , fill="white")
    
def on_right():
    global flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    try:
        words.remove(random_word)
    except ValueError:
        canvas.itemconfig(word_text , text="There is an error. ")
        canvas.itemconfig(lang_text , text="Oops")
        return
    pd.DataFrame(words).to_csv("C:/Users/mdeha/OneDrive/Masaüstü/python/day31/flash_card_project/data/learnedwords.csv", index=False , encoding="utf-8")
    if words:
        next_card()
    else:
        canvas.itemconfig(lang_text , text= "Well Done" , fill="black")
        canvas.itemconfig(word_text , text="You Learned All")
   
def on_wrong():
    global flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    next_card()
#--------------------UI SETUP------------------#
window = Tk()
window.title("Capstone Project")
window.config(padx=50 , pady=50 , bg=BACKGROUND_COLOR)
#----------------Images------------------------#
card_back = PhotoImage(file="C:/Users/mdeha/OneDrive/Masaüstü/python/day31/flash_card_project/images/card_back.png")
card_front = PhotoImage(file="C:/Users/mdeha/OneDrive/Masaüstü/python/day31/flash_card_project/images/card_front.png")
card_right = PhotoImage(file="C:/Users/mdeha/OneDrive/Masaüstü/python/day31/flash_card_project/images/right.png")
card_wrong = PhotoImage(file="C:/Users/mdeha/OneDrive/Masaüstü/python/day31/flash_card_project/images/wrong.png")
#--------------------Canvas--------------------#
canvas = Canvas(height=526 , width=800, bg=BACKGROUND_COLOR , highlightthickness=0)
card_bg = canvas.create_image(400 , 263 , image=card_back, anchor="center")
card_fg = canvas.create_image(400 , 263 , image=card_front, anchor="center")
canvas.grid(row=0 , column=0 , columnspan=2)
lang_text = canvas.create_text(400,150, text="Title", font=LITTLE_FONT)
word_text = canvas.create_text(400,263,text="Example",font=BIG_FONT)
#----------Buttons-------------#
wrong = Button(image=card_wrong , highlightthickness=0 , command=on_wrong)
wrong.grid(row=1 , column=0)
right = Button(image=card_right , highlightthickness=0 , command=on_right)
right.grid(row=1 , column=1)
next_card()
window.mainloop()
