import sqlite3
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
def db():
    return sqlite3.connect('ecogarden.db')
# Cria as tabelas
with db() as c:
    c.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS dispositivos (id INTEGER PRIMARY KEY, nome TEXT, local TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS leituras (id INTEGER PRIMARY KEY, disp_id INT, umidade REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS irrigacao (id INTEGER PRIMARY KEY, disp_id INT, tempo INT)')
# Rota genérica para exibir as telas
@app.route('/<tabela>')
def mostrar(tabela):
    if tabela not in ['usuarios', 'dispositivos', 'leituras', 'irrigacao']:
    con = db()
    dados = con.execute(f'SELECT * FROM {tabela}').fetchall()
    con.close()
    return render_template(f'{tabela}.html', dados=dados)
@app.route('/')
def index():
    return redirect('/dispositivos')
# Rota genérica para cadastrar
@app.route('/add/<tabela>', methods=['POST'])
def adicionar(tabela):
    con = db()
    if tabela == 'usuarios':
        con.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', [request.form.get('nome'), request.form.get('email')])
    elif tabela == 'dispositivos':
        con.execute('INSERT INTO dispositivos (nome, local) VALUES (?, ?)', [request.form.get('nome'), request.form.get('local')])
    elif tabela == 'leituras':
        con.execute('INSERT INTO leituras (disp_id, umidade) VALUES (?, ?)', [request.form.get('disp_id'), request.form.get('umidade')])
    elif tabela == 'irrigacao':
        con.execute('INSERT INTO irrigacao (disp_id, tempo) VALUES (?, ?)', [request.form.get('disp_id'), request.form.get('tempo')])
    con.commit()
    con.close()
    return redirect(f'/{tabela}')
# Rota genérica para deletar
@app.route('/del/<tabela>/<int:id>')
def deletar(tabela, id):
    con = db()
    con.execute(f'DELETE FROM {tabela} WHERE id = ?', [id])
    con.commit()
    con.close()
    return redirect(f'/{tabela}')
if __name__ == '__main__':
    app.run(debug=True)