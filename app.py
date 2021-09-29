import random
import numpy as np
import pickle
import json
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import nltk
from keras.models import load_model
import keras 
from nltk.stem import WordNetLemmatizer

#----------------------------------------
#conda activate dumblebot
#
#
#----------------------------------------

lemmatizer = WordNetLemmatizer()

with open("model/intents_dumbledore.json") as file:
    data = json.load(file)

model = keras.models.load_model('chat_model')

# load tokenizer object
with open('model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('model/label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    res = getResponse(msg)
    return res

def getResponse(msg):
    max_len = 20
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([msg]),
                                             truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            response = np.random.choice(i['responses'])
            response = "Dumblebot: " + response
            return response


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)



