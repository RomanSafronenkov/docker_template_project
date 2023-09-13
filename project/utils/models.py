import base64
from typing import Union

import pandas as pd


class Model:
    @staticmethod
    def base64encode(data: Union[str, int, float]) -> str:
        data = str(data).encode()
        encoded_data = base64.b64encode(data).decode()
        return encoded_data

    def predict(self, data: pd.DataFrame) -> pd.DataFrame:
        for column in data.columns:
            data[column] = data[column].apply(self.base64encode)

        return data
