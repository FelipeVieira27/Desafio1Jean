from flask import Flask, request, render_template,  url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
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
        users = cur.execute("SELECT * FROM contatos")
        userDetails = cur.fetchall()
        cur.close()
        titulo = "Users"
        return render_template("users.html", title = titulo, userDetails=userDetails)
    titulo = "Contatos"
    return render_template ("contato.html", title = titulo)


@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    users = cur.execute("SELECT * FROM contatos")
    titulo = "Users"
    if users > 0:
        userDetails = cur.fetchall()
        return render_template("users.html", titulo = titulo, userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True)