from datetime import date, datetime
from api import API
from managers.linea_manager import LineaManager
from models.direzione import Direzione
from positiondb import PositionDB
from util import Util


# with open('response.html', 'r') as file:
#     html_doc = file.read()

# fermate, max = API.get_corse(6, date(2021,1,7), Direzione.ANDATA)
# print(max)
# corsa = LineaManager.get_corsa(fermate, max-1)
# print(corsa)

# lat, lon = API.get_coordinate_from_address("Via Gioberti Costabissara")
# print(lat, lon)
# res = API.get_linee()
# res.sort(key=lambda x: x['Codice'])
# print(res)

# Util.exportCSV(fermate[0], 'linea 6.csv')


db = PositionDB()
# db.drop_table()
# db.create_table()
# lat, lon = db.get_location("test")
# print(lat, lon)
# db.insert_location("test", 20.3, 22.3)
db.print_all_location()
