import csv
import numpy as np
import matplotlib.pyplot as plt

with open("CoronaDeathsGermany.csv", "r") as csv_file:
    data_reader = csv.reader(csv_file, delimiter=";")
    data_dict = {}
    for row in data_reader:
        data_dict[row[0]] = []
        data = []
        for dat in row:
            if len(dat.split(".")) > 2:
                data.append(dat)
            try:
                data.append(float(dat))
            except ValueError:
                pass
        data_dict[row[0]] = data
print(data_dict.keys())
fig, ax = plt.subplots()
plt.plot(data_dict["Week"], data_dict["Excess Mortality per Week 2020/21"])
plt.plot(data_dict["Week"], data_dict["Diff Corona Deaths per Week 2020/21"])
# plt.plot(data_dict["Date"], data_dict["Diff Corona Deaths per Day 2020/21"])
print(np.corrcoef(data_dict["Deaths per Week 2020/21"], data_dict["Diff Corona Deaths per Week 2020/21"]))
plt.show()
