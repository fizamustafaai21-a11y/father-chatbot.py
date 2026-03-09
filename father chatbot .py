import tkinter as tk
from datetime import datetime
import sqlite3
import pyttsx3
import speech_recognition as sr

# Voice engine
engine = pyttsx3.init()

# Database setup
conn = sqlite3.connect("chat_memory.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user TEXT,
bot TEXT,
time TEXT
)
""")
conn.commit()

father_personality = {
    "hello": "Hello beta! How are you today?",
    "hi": "Hi my child, it feels good to see you happy.",
    "baba": "Ji beta, bolo... kya hua?",
    "abbu": "Haan beta, main yahin hoon. Batao kya baat hai?",
    "i miss you": "I miss you too beta... but remember, I’m always with you in your heart.",
    "love you": "Love you too, my child. You are my pride and my peace.",
    "sad": "Sad mat ho beta... Allah sab theek karega. You’re strong and brave.",
    "angry": "Beta, gussa thoda kam karo... peace se socho, sab theek ho jayega.",
    "tired": "Rest a bit beta, you work hard. I’m proud of you always.",
    "pain": "Dil chhota mat karo beta, I can’t see you in pain. You’ll be fine, InshaAllah.",
    "family": "Always take care of family, beta. That’s real happiness.",
    "friends": "Be kind to your friends, beta. Loyal hearts bring peace.",
    "study": "Study well, beta. Your hard work will make your future bright.",
    "thank you": "No need to thank me beta, fathers never stop loving.",
    "bye": "Khuda hafiz beta, stay strong and happy. I’m always with you."
}

# Get chatbot reply
def get_father_reply(user_input):
    user_input = user_input.lower()
    for key in father_personality:
        if key in user_input:
            return father_personality[key]
    return "Beta, I may not have the perfect words... but I love you and I’m always with you."


def send_message():
    user_msg = user_entry.get()
    if user_msg.strip() == "":
        return
    
    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"You: {user_msg}\n")
    
    reply = get_father_reply(user_msg)
    chat_window.insert(tk.END, f"Father: {reply}\n\n")
    
    chat_window.config(state='disabled')
    engine.say(reply)
    engine.runAndWait()
    
    # Save chat in database with timestamp
    cursor.execute(
        "INSERT INTO chats(user, bot, time) VALUES (?, ?, ?)",
        (user_msg, reply, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    
    # Clear input
    user_entry.delete(0, tk.END)

import tkinter as tk

root = tk.Tk()
root.title("Father Chatbot")
chat_window = tk.Text(root, height=20, width=50, state='disabled', wrap='word', bg="#f4f4f4")
chat_window.pack(pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(side='left', padx=10, pady=10)


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side='left', pady=10)

root.mainloop()
