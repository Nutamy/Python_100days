import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
counts = []
colors = data["Primary Fur Color"].unique()[1:]
print(colors)
for color in colors:
    counts.append(data[data["Primary Fur Color"] == color].shape[0])


df_dict = {
    "Fur color": colors.tolist(),
    "Count": counts
}

df = pd.DataFrame(df_dict)
print(df)
df.to_csv("squirrel_count.csv")
















#
# data_dict = data.to_dict()
# avg_tempr = data["temp"].mean()
# print(data["temp"].min())
#
# print(data[data.temp > 17])


# def cel2fah(cel):
#     fah = (9 / 5.0 * cel) + 32
#     return fah
#
#
# mon_tem = data[data.day == "Monday"].temp
# f_temp_mon = cel2fah(mon_tem)
#
# print(f_temp_mon)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         try:
#             temperature.append(int(row[1]))
#         except:
#             continue
#     print(temperature)
