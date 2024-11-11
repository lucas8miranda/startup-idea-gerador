Gerador de Ideias de Startups

Este projeto é um gerador de ideias para startups, baseado nas informações fornecidas pelo usuário. O aplicativo utiliza a API do OpenAI para criar ideias inovadoras com base em três parâmetros: setor, problema e público-alvo. Ele é uma aplicação web simples, desenvolvida com Flask, e usa a API do OpenAI para processar as informações e gerar uma ideia criativa e única para cada solicitação.

===========================

Como Funciona

A aplicação permite ao usuário preencher três campos:

1. Setor da Startup
2. Problema que a Startup resolve
3. Público-alvo

Após o envio, a aplicação faz uma solicitação para a API do OpenAI, que retorna uma ideia de startup relacionada aos dados fornecidos pelo usuário.

Limitações da API

A API do OpenAI tem limites de taxa para evitar sobrecarga e garantir um uso eficiente. Esses limites são baseados em:

- RPM (Requisições por minuto): Número máximo de solicitações que podem ser feitas por minuto.
- TPM (Tokens por minuto): Número máximo de tokens (unidade de contagem usada pela OpenAI) que podem ser processados por minuto.
- TPD (Tokens por dia): Número máximo de tokens que podem ser processados por dia.

===========================

Estrutura do Projeto

- app.py: Arquivo principal da aplicação Flask. Ele gerencia as rotas e interage com a API do OpenAI.
- index.html: Interface do usuário com um formulário para enviar dados (setor, problema, público-alvo) e receber a ideia de startup gerada.
- .env: Arquivo de configuração onde a chave da API do OpenAI é armazenada.

===========================

Requisitos para Utilizar

Pré-requisitos:
- Python 3.x

Bibliotecas Python necessárias:
- Flask
- Flask-CORS
- OpenAI
- python-dotenv

Instale as dependências:

pip install -r requirements.txt

No arquivo .env altere "OPENAI_API_KEY=sua chave aqui"

===========================

Inicie o Servidor Flask:

python app.py

Em seguida, abra o "index.html" na pasta templates.
