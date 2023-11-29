#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter.ttk import Combobox
import pyttsx3

# Initialize the text-to-speech engine
tts = pyttsx3.init()

# Create the main window
root = tk.Tk()
root.geometry("800x600")
root.title("Text to Speech Converter")

# Add a title to the window with a specific color
title_label = tk.Label(root, text="Text to Speech Converter", font=("Arial", 20), fg="black")
title_label.pack()

# Add a logo to the window
logo_path = "C:\\Users\\Mr\\Downloads\\text to speech.png"  
logo = tk.PhotoImage(file=logo_path)
logo_label = tk.Label(root, image=logo)
logo_label.pack()

# Create a Text widget for entering text
text_box = tk.Text(root, font='calibri 12', wrap=tk.WORD)
text_box.place(x=60, y=250, width=700, height=300)

# Create a Combobox for selecting the voice
voices = tts.getProperty('voices')
voice_var = tk.StringVar(value=voices[0].id)
voice_box = Combobox(root, values=[v.name for v in voices], textvariable=voice_var, state='readonly')
voice_box.place(x=50, y=500, width=200)

# Create a Combobox for selecting the speech rate
speed_var = tk.StringVar(value="150")
speed_box = Combobox(root, values=['50', '100', '150', '200', '250'], textvariable=speed_var, state='readonly')
speed_box.place(x=300, y=500, width=200)

# Create a button to start the text-to-speech conversion
def convert_text_to_speech():
    text = text_box.get(1.0, tk.END)
    selected_voice = voice_var.get()
    selected_speed = int(speed_var.get())
    tts.setProperty('voice', selected_voice)
    tts.setProperty('rate', selected_speed)
    tts.say(text)
    tts.runAndWait()

convert_button = tk.Button(root, text="Convert", command=convert_text_to_speech)
convert_button.place(x=550, y=500)

# Run the main event loop
root.mainloop()


# In[ ]:




