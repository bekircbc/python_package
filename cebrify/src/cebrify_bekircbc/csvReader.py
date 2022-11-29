import csv

data = []

def csvReader(datei):
  with open(datei, newline="") as file:
    csv_file = csv.reader(file, delimiter=";")
    for line in csv_file:
      data.append(line)
      
    return data