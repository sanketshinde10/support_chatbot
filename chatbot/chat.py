import random
import json
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from chatbot.preprocessing import tokenize, stem, bag_of_words

# Load necessary files
model = load_model("models/support_model.h5")

with open("models/words.pkl", "rb") as f:
    words = pickle.load(f)

with open("models/classes.pkl", "rb") as f:
    classes = pickle.load(f)

with open("data/intents.json", "r") as f:
    intents = json.load(f)

def chatbot_response(msg):
    tokens = tokenize(msg)
    bow = bag_of_words(tokens, words)
    bow = np.expand_dims(bow, axis=0)
    result = model.predict(bow)[0]
    threshold = 0.75
    results = [(i, r) for i, r in enumerate(result) if r > threshold]

    if results:
        tag = classes[results[0][0]]
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
    else:
        return "I'm sorry, I didn't understand. Please try again."
