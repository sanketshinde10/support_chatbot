def log_chat(user_input, response):
    with open("logs/chatlog.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nBot: {response}\n\n")
