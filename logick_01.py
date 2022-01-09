import csv
from datetime import datetime

import Parcer


# Exclusive creation of Yields_YYYY-MM-DD.csv returns name of a file on current date
def csv_yields():
    file_name = 'Yields_{0}.csv'.format(str(datetime.date(datetime.today())))
    try:
        with open(file_name, "x", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(Parcer.tables_parse())
        return file_name
    except FileExistsError:
        return file_name


# Exclusive creation of Costs_YYYY-MM-DD.csv returns name of a file on current date
def csv_costs():
    file_name = 'Costs_{0}.csv'.format(str(datetime.date(datetime.today())))
    try:
        with open(file_name, "x", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(Parcer.tables_parse())
        return file_name
    except FileExistsError:
        return file_name
