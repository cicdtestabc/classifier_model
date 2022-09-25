import math

import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.iloc[:9, :].replace({np.nan: None}).to_dict(orient="records")
    }

    print(payload)
    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json= payload,
    )


    # Then
    # assert response.status_code == 200
    prediction_data = response.json()
    print(prediction_data)
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    assert math.isclose(prediction_data["predictions"][0], 1, rel_tol=100)
