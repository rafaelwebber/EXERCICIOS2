import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    cotacao = float(data['USDBRL']['bid'])
    mensagem = f'1 dolar corresponde a R$ {cotacao:.2f}'
    print(mensagem)