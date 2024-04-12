import os
import pytest
from datetime import datetime
from main import read_file, save_to_file, analyze_data

@pytest.fixture
def input_file():
    return os.path.join('data/' 'raw_data.txt')

@pytest.fixture
def output_file():
    return os.path.join('data/' 'result_data.txt')
