from flask import Flask, render_template, jsonify
import serial
import threading
import time

app = Flask(__name__)

# ========== CONFIGURAÇÃO DA PORTA SERIAL ==========
# Substitua 'COM3' pela porta correta do seu Arduino (ex: 'COM4', 'COM5')
porta_arduino = 'COM9' 
baud_rate = 9600
temperatura_atual = 0.0

# Tenta estabelecer conexão com o Arduino
try:
    conexao = serial.Serial(porta_arduino, baud_rate, timeout=1)
    time.sleep(2) # Aguarda o Arduino reiniciar após conectar
    print("✓ Conectado ao Arduino na porta", porta_arduino)
except Exception as e:
    print(f"✗ ERRO DE CONEXÃO: {e}")
    print("O site vai abrir, mas não receberá dados reais. Verifique a porta COM.")
    conexao = None

# Função que roda em segundo plano lendo o Arduino sem travar o site
def ler_arduino():
    global temperatura_atual
    while True:
        if conexao and conexao.in_waiting > 0:
            try:
                # Lê a informação do cabo USB, limpa os espaços e converte para número
                linha = conexao.readline().decode('utf-8').strip()
                if linha: # Só atualiza se a linha não estiver vazia
                    temperatura_atual = float(linha)
            except ValueError:
                # Se vier algum "lixo" na leitura, simplesmente ignora e tenta a próxima
                pass
        time.sleep(0.1)

# Inicia a thread de leitura
thread = threading.Thread(target=ler_arduino, daemon=True)
thread.start()

# --- ROTAS DO SITE ---

# Rota principal: Quando você acessa localhost:5000, ele abre o seu index.html
@app.route('/')
def index():
    return render_template('index.html')

# Rota de Leitura: O site acessa aqui a cada 2 segundos para pegar a temperatura
@app.route('/api/temperatura')
def get_temperatura():
    return jsonify({'temperatura': temperatura_atual})

# Rota de Comando: O site acessa aqui quando você clica no botão de ligar o Ar
@app.route('/api/comando', methods=['POST'])
def enviar_comando():
    if conexao:
        conexao.write(b'A') # Envia a letra 'A' para o Arduino
        conexao.flush() # Força o envio imediato pelo cabo USB
        return jsonify({'status': 'Comando enviado com sucesso!'})
    return jsonify({'status': 'Erro: Arduino desconectado'}), 500

# Inicia o servidor web
if __name__ == '__main__':
    print("Iniciando o servidor... Acesse http://127.0.0.1:5000 no seu navegador.")
    app.run(debug=True, use_reloader=False, port=5000)