# train_model.py
import pandas as pd

data = {
    "text": [
        # Constitution
        "What is the Constitution of India?",
        "When was the Indian Constitution adopted?",
        "Who is known as the father of the Indian Constitution?",
        "How many articles are there in the Constitution?",
        # Fundamental Rights
        "What are Fundamental Rights?",
        "Explain Article 21",
        "What is Article 19 about?",
        "What does Article 32 guarantee?",
        # Fundamental Duties
        "What are Fundamental Duties?",
        "How many Fundamental Duties are there?",
        "Which Article mentions Fundamental Duties?",
        # Directive Principles
        "What are Directive Principles of State Policy?",
        "What is Article 44?",
        "What does Article 39 say?",
        # IPC
        "What is IPC?",
        "What does Section 302 of IPC mean?",
        "Explain Section 420 of IPC",
        "What is Section 498A?",
        # Landmark Cases
        "Tell me about Kesavananda Bharati case",
        "What is the Basic Structure Doctrine?",
        "What did the Supreme Court decide in Kesavananda Bharati?",
        # Preamble
        "What is the Preamble of India?",
        "What are the key words in the Preamble?",
        "When was the Preamble adopted?"
    ],
    "category": [
        "Constitution","Constitution","Constitution","Constitution",
        "Fundamental Rights","Fundamental Rights","Fundamental Rights","Fundamental Rights",
        "Fundamental Duties","Fundamental Duties","Fundamental Duties",
        "Directive Principles","Directive Principles","Directive Principles",
        "IPC","IPC","IPC","IPC",
        "Landmark Case","Landmark Case","Landmark Case",
        "Preamble","Preamble","Preamble"
    ]
}

df = pd.DataFrame(data)
df.to_csv("legal_dataset.csv", index=False)
print("✅ Dataset created successfully!")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle

# Load dataset
df = pd.read_csv("legal_dataset.csv")

# Tokenization
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
padded = pad_sequences(sequences, maxlen=20, padding='post')

# Label encoding
le = LabelEncoder()
y = le.fit_transform(df['category'])

# Model
model = Sequential([
    Embedding(5000, 128, input_length=20),
    Bidirectional(LSTM(128, return_sequences=True)),
    Dropout(0.3),
    Bidirectional(LSTM(64)),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(len(le.classes_), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(padded, y, epochs=60, batch_size=4, verbose=1)

model.save("legal_model.keras")

with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("✅ Model trained and saved successfully!")
