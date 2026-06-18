# Import do framework flask
# Import do render_template para ler o HTML e busca ou o endereço do arquivo ou a URL
# request serve para capturar os dados
from flask import Flask, render_template, request

import mysql.connector 

# Para vincular as páginas e saberem onde estão:

app = Flask(__name__)

# Cria conexão com o mySQL
bd_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro1'
}

# Criação de rota para o arquivo HTML principal

@app.route('/')

def indexRota():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
# Biblioteca mysql.connector conecta o Python com o MySQL
# decorador tem @

def criar_cadastro():
    cpf = request.form['cpf']
    primeiro_nome = request.form['primeiro_nome']
    sobrenome = request.form['sobrenome']
    idade = request.form['idade']

conexao = mysql.connector.connect(**bd_config)

cursor = conexao.cursor()
#É uma função de uma biblioteca do MySql
# ** evita que a gente tenha que digitar o dicionário novamente
# Cursos() : Levar instruções SQL do Python até o banco de dados.

query = "INSERT INTO cliente1(CPF, PRIMEIRO_NOME, SOBRENOME, IDADE) VALUES(%s,%s,%s,%s)"
# %s pega o primeiro campo e substitui o valor. ELe sabe onde está os campos