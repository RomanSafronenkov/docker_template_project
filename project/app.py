import logging

import pandas as pd
from flask import Flask, jsonify, request

from utils.models import Model

logging.basicConfig(format='[%(asctime)s] - [%(levelname)s] - %(message)s',
                    level=logging.INFO)
_LOGGER = logging.getLogger(__name__)
app = Flask(__name__)
model = Model()


@app.route('/predict', methods=['POST'])
def predict():
    _LOGGER.info('Start processing data')
    received_data = request.get_json()
    received_data = pd.DataFrame.from_dict(received_data)

    _LOGGER.info(f'Received data:\n {received_data}')
    response_data = model.predict(received_data)

    _LOGGER.info('Processing finished, returning result')
    return jsonify(response_data.to_dict(orient='split'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
