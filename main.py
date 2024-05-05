from flask import Flask, make_response, jsonify, request
from bd import carros

app = Flask(__name__)
app.config['JSON_SCRT_KEYS'] = False


@app.route('/carros', methods=['GET'])
def getCarros():
    return make_response(
       jsonify(carros)
    )
 
@app.route('/carros', methods=['POST'])   
def createCarro():
    carro = request.json
    carros.append(carro)
    return make_response(
        jsonify(
            message = 'Carro cadastrado com sucesso!',
            carro = carros
        )
    )

app.run()
