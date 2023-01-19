import pytest

from insurance_claim_model.config.core import config
from insurance_claim_model.processing.data_manager import load_dataset


@pytest.fixture()
def sample_input_data():
    return load_dataset(file_name=config.app_config.testing_data_file)
