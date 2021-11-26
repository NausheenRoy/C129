import csv

data=[]
with open("c128.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
planet_data=data[1:]
df = df(df['coloumn_name'].notna())

df["Radius"] = 0.102763*df["Radius"]

df['Mass']=df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["Mass"] = 0.000954588*df["Mass"]


planet_data.sort(key=lambda planet_data:planet_data[2])
with open("DATA_sorted.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)