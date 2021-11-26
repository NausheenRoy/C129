import csv

dataset1=[]
dataset2=[]

with open("c128.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("DATA_sorted.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

header1=dataset1[0]
planetdata1=dataset1[1:]

header2=dataset2[0]
planetdata2=dataset2[1:]

header = header1+header2

planetData=[]
for index, data in enumerate(planetdata1):
    planetData.append(planetdata1[index]+planetdata2[index])

with open("merged.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planetData)