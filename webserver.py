from flask import Flask

from threading import Thread


app = Flask('')


@app.route('/')

def home():

    return "jestem gotowy! Jeśli zaczną wyskakiwać czerwone komunikaty o błędach modułu zresetuj stronę jak dalej nie będzie działać odczekaj 30 minut aby server mógł odpocząć! Miłego niszczenia serwerów"


def run():

  app.run(host='127.0.0.0.',port=8080)


def keep_alive():  

    t = Thread(target=run)

    t.start()