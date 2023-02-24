from datetime import time
from api import API
from models.fermata import Fermata


class LineaManager:

    @staticmethod
    def get_corsa(fermate: list[Fermata], indice: int) -> list:
        corsa = []
        for fermata in fermate:
            orario = fermata.passaggi[indice]
            if len(orario) > 0:
                # status, lat, lon = API.get_coordinate_from_address(fermata.name)
                corsa.append({
                    'fermata': fermata.name,
                    'orario': orario,
                    # 'pos': {
                    #     'lat': lat if status else 0,
                    #     'lon': lon if status else 0
                    # }
                })
        return corsa

    def get_custom_corsa(fermate: list[Fermata], posizione: str, time: time):
        pass