import requests


URL: str = 'http://www.mobilitaveneto.net/TP/SVT/StampaOrari/GetOrariLinea'

data = {
    'di': '07/01/2022',
    'codLineaUtenza': 6,
    'codAzienda': 'SVT',
    'linea': 6,
    'descrLinea': 'Viale Roma-Maddalene-Costabissara-Motta Costabissara',
    'vector': 'SOCIETA VICENTINA TRASPORTI s.r.l.',
    'direzione': 1,
    #'ext': '',
    'df': '07/01/2022'
}
'''
3 Bus
2 Train

'''

r = requests.post(URL, data=data)
print(r.ok)
print(r.content)
if r.ok:
    print(r.content)