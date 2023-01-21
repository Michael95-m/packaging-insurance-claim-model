import pytest

from insurance_claim_model.config.core import DATASET_DIR, config
from insurance_claim_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    test_file = DATASET_DIR / config.app_config.testing_data_file
    return load_dataset(file_name=test_file)
