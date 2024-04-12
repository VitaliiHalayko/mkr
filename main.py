import os
from collections import defaultdict

def read_file(file_path: str) -> list:
    data_from_file = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(', ')
            if len(data) == 3:
                record = {"name": data[0], "date": data[1], "price": data[2]}
                data_from_file.append(record)
    return data_from_file

def analyze_data(data_from_file: list, product_name: str):
    product_data = {}
    for record in data_from_file:
        if record["name"] == product_name:
            product_data.update({record["date"]: record["price"]})

    if product_data == {}:
        return "Product not found"

    return product_data


def main(input_file, output_file):
    product_name = input("Enter product name: ")

    data_from_file = read_file(input_file)

    product_data = analyze_data(data_from_file, product_name)

if __name__ == '__main__':
    input_file = os.path.join('data/' 'raw_data.txt')
    output_file = os.path.join('data/' 'result_data.txt')
    main(input_file, output_file)