from flask import Flask, request, render_template,  url_for
from flask_mysqldb import MySQL

def create_app():
    from app import routes
    routes.init_app(app)

    return app

app = Flask(__name__)

app.config['MYSQL_Host'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'unes'

mysql = MySQL(app)

# Definindo as rotas

@app.route("/")
def home():
    titulo = "Home"
    return render_template ("home.html", title = titulo)

@app.route("/quemsomos")
def quemsomos():
    titulo = "Quem Somos"
    return render_template ("quemsomos.html", title = titulo)

@app.route("/contato", methods=['GET', 'POST'])
def contato_enviado():
    if request.method == "POST":
        email = request.form["email"]
        assunto = request.form["assunto"]
        descricao = request.form["descricao"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES(%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return "Formulário enviado com sucesso!"
    titulo = "Contatos"
    return render_template ("contato.html", title = titulo)


if __name__ == '__main__':
    app.run(debug=True)