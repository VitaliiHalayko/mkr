import os
import pytest
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

@pytest.mark.parametrize('product_names, expected_results, expected_responses', [
    ('Some product', None, 'Product not found'),
    ('Товар1', {'2024-03-15': '100.0', '2024-03-25': '95.0', '2024-04-05': '105.0'}, 'Product was found')
])

def test_analyze_data_product(input_file, product_names, expected_results, expected_responses):
    data = read_file(input_file)
    results, responses = analyze_data(data, product_names)
    assert results == expected_results
    assert responses == expected_responses

