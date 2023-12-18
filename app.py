import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Caminho para o diretório do arquivo de banco de dados
db_path = os.path.join(app.root_path, 'caminho', 'para', 'seu', 'banco-de-dados.db')

@app.route('/agendar', methods=['POST'])
def agendar():
    try:
        # Parâmetros recebidos do formulário
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        data = request.form.get('data')
        horario = request.form.get('horario')
        servico = request.form.get('servico')
        comentario = request.form.get('comentario')

        # Conectar ao banco de dados
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Verificar se o horário está ocupado
        query = "SELECT COUNT(*) FROM agendamentos WHERE horario = ? AND ocupado = 1"
        cursor.execute(query, (horario,))
        horario_ocupado = cursor.fetchone()[0]

        if horario_ocupado > 0:
            return "Horário já ocupado. Escolha outro horário."

        # Inserir o agendamento no banco de dados
        query = "INSERT INTO agendamentos (nome, telefone, email, data, horario, servico, comentario, ocupado) VALUES (?, ?, ?, ?, ?, ?, ?, 1)"
        cursor.execute(query, (nome, telefone, email, data, horario, servico, comentario))

        # Commit para efetivar as mudanças no banco de dados
        conn.commit()

        # Consultar todos os agendamentos
        query = "SELECT * FROM agendamentos"
        cursor.execute(query)
        agendamentos = cursor.fetchall()

        # Imprimir os agendamentos (substitua isso pelo que você deseja fazer)
        for agendamento in agendamentos:
            print(agendamento)

        # Fechar a conexão
        conn.close()

        return "Agendamento bem-sucedido!"
    except Exception as e:
        return f"Erro: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

try:
    # Commit para efetivar as mudanças no banco de dados
    conn.commit()

    print("Agendamento bem-sucedido!")

    # Consultar todos os agendamentos
    query = "SELECT * FROM agendamentos"
    cursor.execute(query)
    agendamentos = cursor.fetchall()

    # Imprimir os agendamentos
    for agendamento in agendamentos:
        print(agendamento)
except Exception as e:
    print(f"Erro: {str(e)}")
