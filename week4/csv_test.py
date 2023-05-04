import csv

csv_path = "sample2.csv"

csv_file = open(csv_path,"a",encoding="utf-8",newline='')

csv_data = csv.reader(csv_file)

