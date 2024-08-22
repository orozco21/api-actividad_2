# Importamos Flask y jsonify (para convertir la lista a JSON).
from flask import Flask, jsonify

app = Flask(__name__)

# Lista de nombres de personas (puedes agregar o modificar según sea necesario)
nombres = [
    "Juan Pablo Gastelbondo",
    "Juan Arrieta afanador",
    "Jonatan romero Fandiño",
    "Adrian Manuel Sanchez",
    "Casandra andrea molina",
    "Enrique orozco perez"
]

# Implementar una ruta en la aplicación Flask que responda a las solicitudes GET en el
# endpoint '/personas'. Esta ruta será la que devuelva la lista de nombres de personas
@app.route('/nombres', methods=['GET'])
def obtener_nombres():
    return jsonify(nombres)

if __name__ == '__main__':
    app.run(debug=True)