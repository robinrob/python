import csv
import operator

class CSVSorter():

    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv
        self.data = []

        with open(self.path_to_csv, 'rb') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            self.data = [row for row in reader]


    def by_col(self, col_num):
        self.data = sorted(self.data, key=operator.itemgetter(col_num), reverse=False)

        return self


    def print_all(self):
        for row in self.data:
            self.print_row(row)


    @staticmethod
    def print_row(row):
        str = ""
        for col in row:
            str += col + " "

        print(str)

