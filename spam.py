import json
import pickle

__model=None

def detect_spam(email):
    result=__model.predict([email])[0]
    if(result==1):
        return "SPAM"
    elif(result==0):
        return "NOT A SPAM"
    else:
        return "ERROR"

def load_saved_artifacts():
    global __model
    with open("./spam_model.pickle","rb") as f:
        __model=pickle.load(f)