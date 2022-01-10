from models.fermata import Fermata

class Util:

    @staticmethod
    def exportCSV(fermate: Fermata, file_name: str) -> None:
        with open(file_name, 'w') as file:
            for fermata in fermate:
                row = fermata.name + ';'
                for passaggio in fermata.passaggi:
                    row += passaggio + ';'
                file.write(row + '\n')