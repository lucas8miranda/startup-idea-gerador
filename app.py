import time
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)

MAX_RPM = 20
MAX_TPM = 50000

last_request_time = None
request_count = 0
tokens_used_this_minute = 0

tokens_used_today = 0
last_day_checked = time.localtime().tm_yday

def update_limits():
    global last_request_time, request_count, tokens_used_this_minute, tokens_used_today, last_day_checked

    current_time = time.time()
    current_minute = time.localtime().tm_min
    current_day = time.localtime().tm_yday

    if last_request_time and (current_time - last_request_time > 60):
        request_count = 0
        tokens_used_this_minute = 0

    if current_day != last_day_checked:
        tokens_used_today = 0
        last_day_checked = current_day

    last_request_time = current_time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerador', methods=['POST'])
def generate_idea():
    global request_count, tokens_used_this_minute, tokens_used_today

    update_limits()

    if request_count >= MAX_RPM:
        return jsonify({'error': 'Limite de requisições por minuto atingido. Tente novamente mais tarde.'}), 429

    if tokens_used_this_minute >= MAX_TPM:
        return jsonify({'error': 'Limite de tokens por minuto atingido. Tente novamente mais tarde.'}), 429

    if tokens_used_today >= MAX_TPM:
        return jsonify({'error': 'Limite de tokens por dia atingido. Tente novamente mais tarde.'}), 429

    data = request.json
    sector = data.get('sector')
    problem = data.get('problem')
    audience = data.get('audience')

    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em geração de ideias de startups."},
                {"role": "user", "content": f"Setor: {sector}, Problema: {problem}, Público-alvo: {audience}"}
            ]
        )

        tokens_used = response['usage']['total_tokens']
        tokens_used_this_minute += tokens_used
        tokens_used_today += tokens_used

        request_count += 1

        idea = response['choices'][0]['message']['content']
        return jsonify({'idea': idea})
    except Exception as e:
        print(f"Erro ao chamar a API do OpenAI: {e}")
        return jsonify({'error': 'Erro ao gerar a ideia.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
