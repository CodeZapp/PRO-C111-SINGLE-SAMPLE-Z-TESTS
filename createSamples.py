import random
import csv
values = []
with open('mediumData.csv', 'r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        values.append(row[7])
print(values)
sample1 = [[values[0]]]
sample2 = [[values[0]]]
sample3 = [[values[0]]]
for i in range(100):
    sample1.append([random.choice(values)])
for i in range(100):
    sample2.append([random.choice(values)])
for i in range(100):
    sample3.append([random.choice(values)])
with open('sample1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample1)
with open('sample2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample2)
with open('sample3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sample3)