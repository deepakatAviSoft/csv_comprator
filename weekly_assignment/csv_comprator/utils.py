import csv

def compare_csv_files(file1, file2):
    csv1_data = [row.decode('utf-8') for row in file1.readlines()]
    csv2_data = [row.decode('utf-8') for row in file2.readlines()]

    if csv1_data == csv2_data:
        return "CSV files are identical."
    else:
        return "CSV files are different."
