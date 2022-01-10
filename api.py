from typing import Tuple
import requests
import os
from datetime import date
from dotenv import load_dotenv
from models.direzione import Direzione
from models.fermata import Fermata
from htmlparser import HtmlParser

class API:
    URL_BASE: str = 'http://www.mobilitaveneto.net/TP/SVT/StampaOrari'
    URL_GET_ORARI_LINEA: str = URL_BASE + '/GetOrariLinea'
    URL_GET_DATI_LINEE: str = URL_BASE + '/GetDatiLineeSelezionate'

    URL_BASE_POSITION: str = 'http://api.positionstack.com/v1/forward'

    @staticmethod
    def get_corse(linea: int, date: date, direction: Direzione) -> Tuple[list[Fermata], int]:
        data = {
            'di': date.strftime("%d/%m/%Y"),
            'linea': linea,
            'direzione': direction.value,
            'codAzienda': 'SVT',
            'ext': '1'
        }
        response = requests.post(API.URL_GET_ORARI_LINEA, data=data)
        fermate = HtmlParser.get_fermate(response.text)

        numero_tratte = min([len(fermata.passaggi) for fermata in fermate])

        return fermate, numero_tratte


    @staticmethod
    def get_linee() -> list:
        data = {
            'vector': 'SOCIETA VICENTINA TRASPORTI s.r.l.',
            'tipo': 3 # 3 Bus, 2 Train
        }
        response = requests.post(API.URL_GET_DATI_LINEE, data=data)
        result = []
        for item in response.json():
            codice_str = item['Codice']
            if codice_str.isdigit():
                codice: int = int(item['Codice'])
                if((codice >= 1 and codice <= 20) or codice == 30):
                    result.append({
                        'Codice': codice,
                        'DestinazioneAndata': item['DestinazioneAndata'],
                        'DestinazioneRitorno': item['DestinazioneRitorno'],
                        'Descrizione': item['Descrizione'],
                        #'DescrizioneAzienda': item['DescrizioneAzienda']
                    })
        result.sort(key=lambda x: x['Codice'])
        return result

    @staticmethod
    def get_coordinate_from_address(address: str) -> Tuple[float, float]:
        load_dotenv()
        api_token = os.getenv('api-positionstack')
        data = {
            'access_key': api_token,
            'query': address,
            'output': 'json'
        }

        response = requests.get(API.URL_BASE_POSITION, params=data)
        data = response.json()['data'][0]
        return data['latitude'], data['longitude']
