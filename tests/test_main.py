import os
import pytest
from datetime import datetime
from main import read_file, save_to_file, analyze_data

@pytest.fixture
def input_test_file():
    return os.path.join('data/' 'test_data.txt')

@pytest.fixture
def input_file():
    return os.path.join('data/' 'raw_data.txt')

@pytest.fixture
def output_file():
    return os.path.join('data/' 'result_data.txt')

def test_read_file(input_test_file):
    assert read_file(input_test_file) == [{'name': 'Товар1', 'date': '2024-03-15', 'price': '100.0'},
                                     {'name': 'Товар2', 'date': '2024-03-20', 'price': '150.0'}]

