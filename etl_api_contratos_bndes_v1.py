import requests
import pandas as pd

url = 'https://dadosabertos.bndes.gov.br/api/3/action/datastore_search'
params = {
    'resource_id': '30f458c0-75d2-4ab1-8218-9a9fa748c1fd',
    'limit': 5,
    'q': 'title:jones'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    records = data['result']['records']  # Extrai os registros da resposta

    # Cria um DataFrame do pandas com os registros
    df = pd.DataFrame.from_records(records)
    
    # Exibe o DataFrame no console
    print(df)
else:
    print("Falha na requisição. Código de status:", response.status_code)
