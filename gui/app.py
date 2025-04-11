import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chatbot.chat import chatbot_response

# Create main window
root = tk.Tk()
root.title("Support Chatbot")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

# Chat display area
chat_log = tk.Text(root, bd=0, bg="white", height=20, width=60, font=("Arial", 12))
chat_log.config(state=tk.DISABLED)
chat_log.pack(padx=10, pady=10)

# Entry box (smaller height)
entry_box = tk.Entry(root, bd=1, bg="white", width=40, font=("Arial", 10))
entry_box.pack(padx=5, pady=(0, 5), side=tk.LEFT, ipady=2)

# Function to send message
def send_message():
    user_msg = entry_box.get().strip()
    entry_box.delete(0, tk.END)
    if user_msg:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"You: {user_msg}\n")
        bot_response = chatbot_response(user_msg)
        chat_log.insert(tk.END, f"Bot: {bot_response}\n\n")
        chat_log.config(state=tk.DISABLED)
        chat_log.see(tk.END)

# Send button
send_button = tk.Button(root, text="Send", width=10, height=2, bg="blue", fg="white", command=send_message)
send_button.pack(padx=10, pady=(0, 10), side=tk.RIGHT)

# Run app
root.mainloop()
