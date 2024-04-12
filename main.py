import os
import matplotlib.pyplot as plt
from datetime import datetime

# read file function
def read_file(file_path: str) -> list:
    """
    :param file_path: path of the file
    :return: list of dictionaries about the products in file
    """
    data_from_file = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(', ')
            if len(data) == 3:
                record = {"name": data[0], "date": data[1], "price": data[2]}
                data_from_file.append(record)
    return data_from_file

# save to file function
def save_to_file(product_data: dict, product_name: str, file_path: str) -> None:
    """
    :param product_data: list of dictionaries about the products
    :param product_name: product name
    :param file_path: path of the file
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Product name: {product_name}\n")

        prev_price = None
        for date, price in product_data.items():
            if prev_price is not None:
                price_change = float(price) - float(prev_price)
                if price_change > 0:
                    file.write(f"{date}: price: {price} | Price increased by {price_change}\n")
                elif price_change < 0:
                    file.write(f"{date}: price: {price} | Price decreased by {abs(price_change)}\n")
                else:
                    file.write(f"{date}: price: {price} | Price remained unchanged\n")
            else:
                file.write(f"{date}: price: {price}\n")
            prev_price = price

# analyze data from file function
def analyze_data(data_from_file: list, product_name: str) -> (dict, str):
    """
    :param data_from_file: list of dictionaries about the products
    :param product_name: product name
    :return: dictionary about the products prices and response
    """
    product_data = {}
    for record in data_from_file:
        if record["name"] == product_name:
            product_data.update({record["date"]: record["price"]})

    if product_data == {}:
        return None, "Product not found"

    return product_data, "Product was found"

# show data function
def show_data(product_data: dict, product_name: str) -> None:
    """
    :param product_data: dictionary about the product
    :param product_name: product name
    """
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

# main function
def main(input_file, output_file):
    product_name = input("Enter product name: ")

    data_from_file = read_file(input_file)

    product_data, response = analyze_data(data_from_file, product_name)

    if response == "Product was found":
        show_data(product_data, product_name)
        save_to_file(product_data, product_name, output_file)
    else:
        print("Invalid product name. Please input a valid product name")
        main(input_file, output_file)

# start
if __name__ == '__main__':
    input_file = os.path.join('data/' 'raw_data.txt')
    output_file = os.path.join('data/' 'result_data.txt')
    main(input_file, output_file)