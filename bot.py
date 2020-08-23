from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import random

conversations = [
    ['Hi',
    'Hi There!',
    'How are you?',
    'Great!'], 
    ['What\'s your favorite',
    'Inception'
    ],
    ['What\'s your favorite song?',
    'Metropolis by Logic',
    'Me too!'
    ],
    ['Do you like books?',
    'Yes'
    ],
    ['My name is',
    'Nice to meet you!'],
    ['Inception', 
    'I love it!']
]
formulas = [
    ['area circle',
    'pi times r squared!'], 
    ['Pythagorean Theorem',
    'a squared plus b squared equals c squared!']
]
no_response = [
    'Very Nice!',
    'That\'s great!',
    'I am a Bot Man',
    'Me too',
    'What\'s your favorite Movie?'
]
chatbot = ChatBot('Bot Man')
trainer = ListTrainer(chatbot)
[trainer.train(x) for x in conversations]
[trainer.train(x) for x in formulas]

trainer2 = ChatterBotCorpusTrainer(chatbot)

trainer2.train(
    "chatterbot.corpus.english"
)


print('Hi There, My name is Mr Bot Man.')
while(True):
    try:
        response = chatbot.get_response(input())
        print(response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    except (AttributeError):
        print(random.choice(no_response))