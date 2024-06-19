from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template("home.html")

# Rota que renderiza uma página HTML
@app.route('/sobre')
def pagina_html():
    return render_template('sobre.html')

@app.route('/curso')
def curso_html():
    return render_template('curso.html')

@app.route('/curso_ambiente')
def curso_amb_html():
    return render_template('curso_ambiente.html')

# Rota com variável na URL
@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)