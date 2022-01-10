from enum import Enum
class Direzione(Enum):
    ANDATA = 1
    RITORNO = 2

    def __str__(self) -> str:
        if self.value == 1:
            return 'Andata'
        return 'Ritorno'