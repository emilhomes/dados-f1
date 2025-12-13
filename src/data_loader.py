import requests
import pandas as pd

base_url = 'https://api.jolpi.ca/ergast/f1/2023/results.json'
limit = 100
offset = 0

race_list = []

while True:
    url = f"{base_url}?limit={limit}&offset={offset}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Sucesso!")
    else:
        print(f"Falha na requisição. Código de status: {response.status_code}")
        print(f"Motivo: {response.reason}")

    data = response.json()

    print("Chaves na raiz: ", data.keys())

    races = data['MRData']['RaceTable']['Races']

    if not races:
        break

    for race in races:
        for result in race['Results']:
            record = {
                'Name': race['raceName'],
                'Date': race['date'],
                'Round': race['round'],
                'Url': race['url'],
                'Driver': result['Driver']['driverId'],
                'Constructor': result['Constructor']['constructorId'],
                'Grid': result['grid'],
                'Position': result['position'],
                'Status': result['status'],
                'Points': result['points'],
                'Time_Millis': result.get('Time', {}).get('millis'),
                'Fastest_Lap_Rank': result.get('FastestLap', {}).get('rank'),
                'Fastest_Lap_Time': result.get('FastestLap', {}).get('Time', {}).get('time')
            }

            race_list.append(record)

    offset += limit #vai para a próxima página


df = pd.DataFrame(race_list)
print(f"Total de linhas capturadas: {len(df)}")
df.to_csv("data/raw/races_2023.csv", index=False)