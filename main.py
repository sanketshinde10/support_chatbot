import json
import numpy as np
import pickle
from tensorflow.keras.utils import to_categorical
from chatbot.preprocessing import tokenize, stem, bag_of_words
from chatbot.model import build_model

# Load intents
with open('data/intents.json') as file:
    intents = json.load(file)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?', '!', '.', ',']
all_words = sorted(set(stem(w) for w in all_words if w not in ignore_words))
tags = sorted(set(tags))

X_train = []
y_train = []

for (pattern_sentence, tag) in xy:
    bow = bag_of_words(pattern_sentence, all_words)
    X_train.append(bow)
    y_train.append(tags.index(tag))

X_train = np.array(X_train)
y_train = to_categorical(np.array(y_train))

# Save words and classes
with open('models/words.pkl', 'wb') as f:
    pickle.dump(all_words, f)

with open('models/classes.pkl', 'wb') as f:
    pickle.dump(tags, f)

# Build and train model
model = build_model(len(X_train[0]), len(tags))
model.fit(X_train, y_train, epochs=200, batch_size=8, verbose=1)
model.save("models/support_model.h5")

print("Training complete. You can now chat with the bot.")

# Optionally: chat loop
from chatbot.chat import chatbot_response

while True:
    msg = input("You: ")
    if msg.lower() in ["quit", "exit"]:
        break
    print("Bot:", chatbot_response(msg))
