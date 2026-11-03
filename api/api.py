import requests
import os
from dotenv import load_dotenv

#Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera as informações
chave = os.getenv('API_KEY')
url = os.getenv('URL_WEATHER')

# Geração dos parâmetros
parametros = {
    "q": "Natal,BR",    # Cidade/Código do País (ISO 3166)
    "appid": chave,
    "units": "metric",  # Temperatura para °C e Vento para M/S
    "lang": "pt_br"     # Descrição do Tempo em PT-BR
}

resposta = requests.get(url, params=parametros, timeout=10)

# Tratando se a resposta tem código válido
if resposta.status_code == 200:
    print("Status: ", resposta.status_code)
    dados = resposta.json()

else:
    print(f'Erro na consulta:', resposta.status_code)

# Mostra os dados
print(f'Cidade:', dados["name"], '–', dados["sys"]["country"])
