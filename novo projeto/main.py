from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Olá mundo!!</h1>'

@app.route("/sobre")
def sobre():
    return '<h1>Sou pessoa legal!</h1>'

@app.route("/sobre/idade")
def idade():
    return '<h1>Eu tenho 14 anos.</h1>'

@app.route("/sobre/endereco")
def endereco():
    return "<h1>Eu moro no Brasil</h1>"

app.run(debug=True)