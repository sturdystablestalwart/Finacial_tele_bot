import csv


def csv_read(filename):
    file_name = filename
    csv_row_list = []
    with open(file_name, "r") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            csv_row_list.append(row)
    return csv_row_list
