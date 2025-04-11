### 📁 Support Chatbot – README

A simple AI-powered support chatbot using **NLTK**, **TensorFlow**, and **Tkinter GUI**, trained on predefined intents using a neural network.

---

### 🧠 Features

- NLP-powered intent recognition (tokenizing, stemming, bag-of-words)
- Trained using Keras and TensorFlow
- GUI-based chat app with Tkinter
- Modular structure (chatbot logic, GUI, training separated)
- Customizable intents in JSON format
- Chat logs stored locally

---

### 🗂 Project Structure

```bash
support_chatbot/
│
├── chatbot/                  # Core chatbot logic
│   ├── __init__.py
│   ├── chat.py               # Generates responses
│   ├── model.py              # Defines & builds the model
│   ├── preprocessing.py      # Tokenizer, stemmer, BOW, etc.
│   └── utils.py              # Any utility functions
│
├── data/
│   └── intents.json          # Predefined intents (Q&A patterns)
│
├── gui/
│   └── app.py                # Tkinter GUI interface
│
├── logs/
│   └── chatlog.txt           # Stores past chats
│
├── models/
│   ├── support_model.h5      # Trained Keras model
│   ├── words.pkl             # Vocabulary
│   └── classes.pkl           # Intents/classes
│
├── .gitignore                # To ignore unnecessary files/folders
├── main.py                   # Run this to train and interact via console
├── requirements.txt          # All required dependencies
└── README.md                 # This file
```

---

### 🚀 Setup & Run Instructions

#### 1. Clone the repository

```bash
git clone https://github.com/your-username/support_chatbot.git
cd support_chatbot
```

#### 2. Create and activate a virtual environment (recommended)

Using **conda**:

```bash
conda create -n support_bot python=3.11
conda activate support_bot
```

Or using **venv**:

```bash
python -m venv support_bot_venv
.\support_bot_venv\Scripts\activate   # Windows
source support_bot_venv/bin/activate # Mac/Linux
```

---

#### 3. Install requirements

```bash
pip install -r requirements.txt
```

---

#### 4. Train the Model

```bash
python main.py
```

It will generate:
- `models/support_model.h5`
- `models/words.pkl`
- `models/classes.pkl`

---

#### 5. Run the GUI Chatbot

```bash
python gui/app.py
```

---

### 📚 Customize Your Bot

You can edit `data/intents.json` to add new tags, questions, and responses:
```json
{
  "tag": "greeting",
  "patterns": ["Hi", "Hello", "Hey"],
  "responses": ["Hi! How can I help you?"]
}
```

After changes, **retrain** using:

```bash
python main.py
```

---

### 🛑 .gitignore Sample

```gitignore
__pycache__/
*.pyc
*.pkl
*.h5
*.log
*.txt
support_chatbot_venv/
.env
.vscode/
```

---

