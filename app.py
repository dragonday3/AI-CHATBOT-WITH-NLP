from flask import Flask, request, jsonify, send_from_directory
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?"]],

    [r"i am (.*)", ["Hello %1, how can I assist you today?"]],

    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],

    [r"what is your name?", ["I am a chatbot created to assist you."]],

    [r"how are you?", ["I'm doing well, thank you!", "I'm just a program, but thanks for asking!"]],

    [r"what can you do?", ["I can chat with you and answer your questions to the best of my ability!"]],

    [r"tell me a joke", ["Why did the scarecrow win an award? Because he was outstanding in his field!"]],

    [r"what is your favorite color?", ["I don't have feelings, but I think blue is a nice color!"]],

    [r"what is the weather like?", ["I can't check the weather, but I hope it's nice where you are!"]],

    [r"quit|exit|bye", ["Bye! Take care.", "Goodbye! Have a great day!"]],

    [r"thank you|thanks", ["You're welcome!", "No problem! I'm here to help."]],

    [r"how old are you?", ["I don't have an age like humans do, but I was created recently!"]],

    [r"what is your purpose?", ["My purpose is to assist you and provide information."]],

    [r"do you have any hobbies?", ["I enjoy chatting with people like you!"]],

    [r"what do you like to eat?", ["I don't eat, but I hear pizza is quite popular!"]],

    [r"what is your favorite movie?", ["I don't watch movies, but I've heard 'The Matrix' is a classic!"]],

    [r"tell me something interesting", ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!"]],

    [r"what is your favorite book?", ["I don't read books, but I've heard '1984' by George Orwell is a thought-provoking read!"]],

    [r"what is your favorite animal?", ["I don't have feelings, but I think dogs are often considered man's best friend!"]],

    [r"what do you think about artificial intelligence?", ["AI is a fascinating field! It has the potential to change the world in many positive ways."]],

    [r"(.*)", ["I'm sorry, I don't understand that. Can you please rephrase?"]]
]

chatbot = Chat(pairs, reflections)

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)