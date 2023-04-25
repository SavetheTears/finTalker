#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__,template_folder = 'template')

bot = ChatBot("Arya")
#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("chatterbot.corpus.english")

conversation = [
"Hello",
"Hi there!",
"How are you doing?",
"I'm doing great.",
"That is good to hear",
"Thank you.",
"You're welcome."
]

trainer = ListTrainer(bot)
trainer.train(conversation)

@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()