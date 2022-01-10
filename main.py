from datetime import date, datetime
from api import API
from managers.linea_manager import LineaManager
from models.direzione import Direzione
from util import Util


# with open('response.html', 'r') as file:
#     html_doc = file.read()

fermate, max = API.get_corse(6, date(2021,1,7), Direzione.ANDATA)
print(max)
corsa = LineaManager.get_corsa(fermate, max-1)
print(corsa)

# res = API.get_linee()
# res.sort(key=lambda x: x['Codice'])
# print(res)

# Util.exportCSV(fermate[0], 'linea 6.csv')
