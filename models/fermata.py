class Fermata:
    def __init__(self, name) -> None:
        self.name = name
        self.passaggi: str = []

    def add(self, orario:str) -> None:
        self.passaggi.append(orario.strip())

    def __str__(self) -> str:
        fermate_Str = self.name + '\n'
        for passaggio in self.passaggi:
            fermate_Str += passaggio + ' '
        return fermate_Str.strip()
