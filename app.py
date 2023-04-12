from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    titulo = "Home"
    return render_template ("home.html", title = titulo)

@app.route("/home.html")
def home2():
    titulo = "Home"
    return render_template ("home.html", title = titulo)

@app.route("/quemsomos.html")
def quemsomos():
    titulo = "Quem Somos"
    return render_template ("quemsomos.html", title = titulo)

@app.route("/contato.html")
def contato():
    titulo = "Contato"
    return render_template ("contato.html", title = titulo)