import nltk
from model import * # Imports my model.py file
import streamlit as st
from streamlit_chat import message

# Load the model in
try:
    model.load("model.tflearn")
except:
    print("Cannot load model")

# Chat function that ties everything together andd prompts the user
def chat(inp):
    print("The bot is ready to talk!!(Type 'quit' to exit)")
    #while True:
    #inp = input("\nYou: ")
        #if inp.lower() == 'quit':
            #break

    #Probability of correct response 
    results = model.predict([bag_of_words(inp, words)])

    # Picking the greatest number from probability
    results_index = np.argmax(results)

    tag = labels[results_index]


    for tg in data['intents']:

        if tg['tag'] == tag:
            responses = tg['responses']

    #print("Bot:" + random.choice(responses))
    return random.choice(responses)



user_input = st.text_input("label goes here")
message(user_input, is_user=True)

# Zeebot response
message(chat(user_input))

