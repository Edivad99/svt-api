from models.fermata import Fermata


class LineaManager:

    @staticmethod
    def get_corsa(fermate: list[Fermata], indice: int) -> list:
        corsa = []
        for fermata in fermate:
            orario = fermata.passaggi[indice]
            if len(orario) > 0:
                corsa.append({
                    'fermata': fermata.name,
                    'orario': orario
                })
        return corsa