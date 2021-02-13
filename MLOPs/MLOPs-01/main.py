from flask import Flask
from textblob import TextBlob

app = Flask('meu_app')

@app.route('/')
def home():
    return "Minha Primeira API."

@app.route('/sentimento/<frase>')
def sentimentos(frase):
	tb = TextBlob(frase)
	tb_en = tb.translate(to='en')
	polaridade = tb_en.sentiment.polarity
	return "polaridade: {}".format(polaridade)

app.run(debug=True)
