from datetime import datetime
from flask import Flask, request, jsonify
from api import API
from managers.linea_manager import LineaManager
from models.direzione import Direzione

app = Flask(__name__)

@app.route("/api/linea/<int:numero>")
def get_linea(numero):
    data = request.args.get('data', "2021-01-07")
    direzione = int(request.args.get('direzione', 1))

    date = datetime.strptime(data, '%Y-%m-%d').date()

    fermate, max_tratte = API.get_corse(numero, date, Direzione(direzione))

    corsa = LineaManager.get_corsa(fermate, 6)#TODO: Cambiare il 6

    return {
        'data': date.strftime("%d/%m/%Y"),
        'numeroLinea': numero,
        'maxTratte': max_tratte,
        'direzione': str(Direzione(direzione)),
        'fermate': corsa
    }

@app.route("/api/linea")
def get_linee():
    linee = API.get_linee()
    linee.sort(key=lambda x: x['Codice'])
    return jsonify(linee)
