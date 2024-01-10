import requests
from flask import Flask, jsonify # Subi o projeto utilizando a biblioteca Flask

app = Flask(__name__)

link = "http://economia.awesomeapi.com.br/json/last/USD-BRL" # Link onde pego o valor do dólar

@app.route('/dolar_atual', methods=['GET']) # Rota que o utilizei com o método GET
def get_dollar_rate():
    try:

        valor_dolar = requests.get(link)

        if valor_dolar.status_code == 200: # Verifico se o servidor retorna código 200 (OK)

            valor_dolar_json = valor_dolar.json()
            cotacao_dolar = valor_dolar_json.get("USDBRL")  # Acesso o objeto USDBRL

            return jsonify({'dollar_rate': cotacao_dolar}) # Retorno o objeto em Json para quem fez a requisição
        
        else:

            return jsonify({'error': 'Cotacao do dolar nao encontrada'}), 404 # Retorna um JSON com erro 404

    except requests.RequestException as e:

        return jsonify({'error': 'Erro ao acessar a cotacao do dolar'}), 500 # Retorna um JSON com erro 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Local que será executado o projeto, nesse caso: http://localhost:5000
