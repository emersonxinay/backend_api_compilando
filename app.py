from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Habilitar CORS para que React pueda hacer peticiones
CORS(app)


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "¡Hola desde Flask!",
        "items": ["item1", "item2", "item3"]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
