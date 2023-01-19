import math

import numpy as np

from insurance_claim_model.predict import predict_data


def test_make_prediction(sample_input_data):

    expected_first_prediction_value = 4466.273966383627
    expected_no_predictions = 268

    # When
    result = predict_data(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=10000)
