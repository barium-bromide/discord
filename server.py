from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "Bot is alive"


def run():
    t = Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 10000})
    t.start()