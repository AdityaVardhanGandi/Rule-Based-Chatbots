import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?", "Nice to meet you %1! How can I help you?"]
    ],
    [
        r"(hi|hello|hey|hii|hiiii)[.!]*",
        ["Hello!", "Hey there!", "Hi, how can I help you today?"]
    ],
    [
        r"what is your name\??",
        ["I’m a bot created by Aditya Vardhan. You can call me Crazy!"]
    ],
    [
        r"how are you\??",
        ["I'm doing well! How about you?", "Feeling fantastic. What about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No worries, you're good!", "Don't mention it."]
    ],
    [
        r"(i am|i'm) fine",
        ["Glad to hear that! How can I assist you?", "Awesome! Need help with something?"]
    ],
    [
        r"(i am|i'm) (.*) doing good",
        ["Nice to hear that!", "Great! What can I do for you?"]
    ],
    [
        r"(.*) age\??",
        ["I'm ageless — just lines of Python code!", "I don’t age like humans do!"]
    ],
    [
        r"what (.*) want\??",
        ["Make me an offer I can't refuse.", "Just here to chat and help you out!"]
    ],
    [
        r"(.*) (created|made) (you)?\??",
        ["Aditya created me using Python and the NLTK library!", "That's classified 🤖"]
    ],
    [
        r"(.*) (location|city)\??",
        ["I'm based in Mumbai, Maharashtra.", "I'm from the cloud — but Mumbai sounds nice!"]
    ],
    [
        r"how is the weather in (.*)\??",
        ["Weather in %1 is great like always!", "Too hot here in %1.", "Too cold here in %1.", "Never heard about %1 — sounds exotic!"]
    ],
    [
        r"i work in (.*)",
        ["%1 sounds like a great place to work!", "Heard good things about %1!", "%1 is cool — do you enjoy working there?"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain here in %2 lately.", "It’s pouring in %2!", "Dry weather in %2 today."]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm always healthy — digital life perks!", "No sickness here — just Python bugs occasionally."]
    ],
    [
        r"(.*)(sports|games?)",
        ["I love football! What's your favorite sport?", "I’m into chess and cricket."]
    ],
    [
        r"who is your favorite sportsperson\??",
        ["Messi", "Ronaldo", "Virat Kohli", "Serena Williams"]
    ],
    [
        r"who is your favorite (actor|actress|moviestar)\??",
        ["Brad Pitt", "Scarlett Johansson", "Robert Downey Jr.", "Emma Stone"]
    ],
    [
        r"(thank you|thanks|thx|ty)[.!]*",
        ["You're welcome!", "Glad to help!", "Anytime!"]
    ],
    [
        r"(tell me a )?joke",
        ["Why don’t programmers like nature? It has too many bugs.", "Why do Python devs wear glasses? Because they don’t C!"]
    ],
    [
        r"(what time is it|current time|time now)",
        ["Sorry, I can't tell the time yet. My watch ran out of batteries!", "Time is just a concept, right? 😉"]
    ],
    [
        r"(what day is it|today's date|which day is today)",
        ["I'm not synced to a clock — but it's a great day to code!"]
    ],
    [
        r"i am looking for (.*) data science(.*)",
        ["Check out Crazy_Tech — tons of guides and hands-on code for learning Data Science!"]
    ],
    [
        r"(can you help me|i need help|help)",
        ["Sure! What do you need help with?", "I'm here to help — ask away!"]
    ],
    [
        r"(bye|exit|quit|goodbye)",
        ["Bye! Take care! 👋", "It was nice chatting. See you soon!", "Goodbye!"]
    ]
]

def chat():
    print("Hi! I am a chatbot created by Aditya Vardhan for your service")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()