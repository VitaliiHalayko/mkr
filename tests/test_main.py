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

def test_save_to_file(input_test_file, output_file):
    product_data = {'2024-03-15': '100.0', '2024-03-20': '150.0'}
    save_to_file(product_data, 'Product1', output_file)
    with open(output_file, 'r') as file:
        content = file.read()
        assert 'Product name: Product1' in content
        assert '2024-03-15: price: 100.0' in content
        assert '2024-03-20: price: 150.0 | Price increased by 50' in content

