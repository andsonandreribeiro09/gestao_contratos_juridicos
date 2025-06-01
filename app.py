from flask import Flask, render_template, request, redirect
import psycopg2
import os


app = Flask(__name__)

# Conexão com PostgreSQL Render
def connect_db():
    return psycopg2.connect(
        host = 'dpg-d0if6jodl3ps73cjqnng-a.oregon-postgres.render.com',
        database='pingpong_grjk',
        user='pingpong_grjk_user',
        password='zwwUd1vJIY9W7pQZ9hasoxbDuZzB4h5I',
        port="5432"
    )


# Inicializar tabelas
def init_db():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            idCliente SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS contratos (
            idContrato SERIAL PRIMARY KEY,
            numero TEXT,
            valor REAL,
            dataAssinatura DATE,
            idCliente INTEGER REFERENCES clientes(idCliente)
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = connect_db()
    c = conn.cursor()

    # Filtro de valor
    valor_min = request.args.get('valor_min', 0, type=float)
    valor_max = request.args.get('valor_max', 100000, type=float)
    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()
    c.execute("SELECT * FROM contratos WHERE valor BETWEEN %s AND %s", (valor_min, valor_max))
    contratos = c.fetchall()

    conn.close()
    return render_template("index.html", clientes=clientes, contratos=contratos)

@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    nome = request.form['nome']
    cpf = request.form['cpf']
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/add_contrato', methods=['POST'])
def add_contrato():
    numero = request.form['numero']
    valor = float(request.form['valor'])
    data = request.form['data']
    idCliente = int(request.form['idCliente'])

    conn = connect_db()
    c = conn.cursor()

    # Verificar se o cliente existe
    c.execute('SELECT idCliente FROM clientes WHERE idCliente = %s', (idCliente,))
    cliente = c.fetchone()
    if cliente is None:
        conn.close()
        return "Erro: Cliente não encontrado. Insira um cliente válido antes de adicionar um contrato.", 400

    # Inserir contrato
    c.execute('''INSERT INTO contratos (numero, valor, dataAssinatura, idCliente)
                 VALUES (%s, %s, %s, %s)''', (numero, valor, data, idCliente))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete_cliente/<int:idCliente>', methods=['POST'])
def delete_cliente(idCliente):
    conn = connect_db()
    c = conn.cursor()
    try:
        # Deleta contratos relacionados ao cliente
        c.execute('DELETE FROM contratos WHERE idCliente = %s', (idCliente,))
        
        # Deleta o cliente
        c.execute('DELETE FROM clientes WHERE idCliente = %s', (idCliente,))
        
        conn.commit()
    except Exception as e:
        conn.rollback()
        return f"Erro ao excluir cliente: {str(e)}", 500
    finally:
        conn.close()

    return redirect('/')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
