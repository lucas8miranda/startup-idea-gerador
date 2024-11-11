Gerador de Ideias de Startups

Este projeto é um gerador de ideias para startups baseado em informações fornecidas pelo usuário. O aplicativo usa a API do OpenAI para gerar ideias de startups com base em três parâmetros: setor, problema e público-alvo. Ele é uma aplicação web simples, desenvolvida com Flask, e usa a API do OpenAI para processar as informações e gerar uma ideia criativa

===========================

COMO FUNCIONA..

A aplicação permite ao usuário preencher três campos:

1 - Setor da Startup
2 - Problema que a Startup resolve
3 - Público-alvo

Após o envio, a aplicação faz uma solicitação para a API do OpenAI, que retorna uma ideia de startup relacionada aos dados informados.

A API tem limites de taxa para evitar sobrecarga. Os limites são baseados em:

RPM (Requisições por minuto): número máximo de solicitações que podem ser feitas por minuto.
TPM (Tokens por minuto): número máximo de tokens (unidade de contagem usada pela OpenAI) que podem ser processados por minuto.
TPD (Tokens por dia): número máximo de tokens que podem ser processados por dia.

===========================

ESTRUTURA DO PROJETO..

app.py: Arquivo principal da aplicação Flask que gerencia as rotas e interage com a API do OpenAI.
index.html: Interface do usuário com um formulário para enviar dados (setor, problema, público-alvo) e receber uma ideia de startup gerada.
.env: Arquivo de configuração para armazenar a chave da API do OpenAI.

Este projeto é um gerador de ideias para startups baseado em informações fornecidas pelo usuário. O aplicativo usa a API do OpenAI para gerar ideias de startups com base em três parâmetros: setor, problema e público-alvo. Ele é uma aplicação web simples, desenvolvida com Flask, e usa a API do OpenAI para processar as informações e gerar uma ideia criativa.

Como Funciona
A aplicação permite ao usuário preencher três campos:

Setor da Startup
Problema que a Startup resolve
Público-alvo
Após o envio, a aplicação faz uma solicitação para a API do OpenAI, que retorna uma ideia de startup relacionada aos dados informados.

A API tem limites de taxa para evitar sobrecarga. Os limites são baseados em:

RPM (Requisições por minuto): número máximo de solicitações que podem ser feitas por minuto.
TPM (Tokens por minuto): número máximo de tokens (unidade de contagem usada pela OpenAI) que podem ser processados por minuto.
TPD (Tokens por dia): número máximo de tokens que podem ser processados por dia.
Estrutura do Projeto
app.py: Arquivo principal da aplicação Flask que gerencia as rotas e interage com a API do OpenAI.
index.html: Interface do usuário com um formulário para enviar dados (setor, problema, público-alvo) e receber uma ideia de startup gerada.
.env: Arquivo de configuração para armazenar a chave da API do OpenAI.

===========================

REQUISITOS PARA ULTILIZAR..

Pré-requisitos:
Python 3.x

Bibliotecas Python:
Flask
Flask-CORS
OpenAI
python-dotenv

Instale as dependências:

Copiar código
pip install -r requirements.txt

No arquivo .env altere "OPENAI_API_KEY=sua chave aqui"

===========================

INICIE O SERVIDOR FLASK:

python app.py

EM SEGUIDA ABRA O "index.html" na pasta templates.

===========================