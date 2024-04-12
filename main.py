import os

def read_file(file_path: str) -> list:
    data_from_file = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(', ')
            if len(data) == 3:
                record = {"name": data[0], "date": data[1], "price": data[2]}
                data_from_file.append(record)
    return data_from_file

def main(input_file, output_file):

if __name__ == '__main__':
    input_file = os.path.join('data' 'raw_data.txt')
    output_file = os.path.join('data' 'result_data.txt')
    main(input_file, output_file)