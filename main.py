from datetime import date, datetime
from api import API
from managers.linea_manager import LineaManager
from models.direzione import Direzione


# with open('response.html', 'r') as file:
#     html_doc = file.read()

# fermate = API.get_corse(1, date(2021,1,7), Direzione.ANDATA)
# print(fermate[1])
# corsa = LineaManager.get_corsa(fermate, 7)
# print(corsa)

res = API.get_linee()
res.sort(key=lambda x: x['Codice'])
print(res)

#Util.exportCSV(fermate, 'linea 6.csv')
