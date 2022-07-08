import csv
from wsgiref import headers

data=[]
with open("archive_dataset.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append (row)

header=data[0]
planet_data=data[1:]

for data_point in planet_data:
    data_point[2]=data_point[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("archive_dataset_sorted.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planet_data)

with open("archive_dataset_sorted.csv")as input,open("archive_dataset_sorted1.csv","w",newline="")as output:
    write=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row):
            write.writerow(row)
