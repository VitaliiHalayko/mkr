import os
import matplotlib.pyplot as plt
from datetime import datetime

def read_file(file_path: str) -> list:
    data_from_file = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(', ')
            if len(data) == 3:
                record = {"name": data[0], "date": data[1], "price": data[2]}
                data_from_file.append(record)
    return data_from_file


def analyze_data(data_from_file: list, product_name: str) -> (dict, str):
    product_data = {}
    for record in data_from_file:
        if record["name"] == product_name:
            product_data.update({record["date"]: record["price"]})

    if product_data == {}:
        return None, "Product not found"

    return product_data, "Product was found"


def show_data(product_data: dict, product_name: str):
    dates = [datetime.strptime(date, "%Y-%m-%d") for date in product_data.keys()]
    prices = [float(price) for price in product_data.values()]

    plt.plot(dates, prices, marker='o', linestyle='-')
    plt.title(f"Price changes for {product_name}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main(input_file, output_file):
    product_name = input("Enter product name: ")

    data_from_file = read_file(input_file)

    product_data, response = analyze_data(data_from_file, product_name)

    show_data(product_data, product_name)



if __name__ == '__main__':
    input_file = os.path.join('data/' 'raw_data.txt')
    output_file = os.path.join('data/' 'result_data.txt')
    main(input_file, output_file)