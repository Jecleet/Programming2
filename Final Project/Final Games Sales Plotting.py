import csv
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/james/PycharmProjects/P2_SP20/Final Project/vgsales.csv')
print(df.head())

list_platform = [f for f in df['Platform']]
print(list_platform)

all_type_platform = set(list_platform)
print(all_type_platform)

index_PS = []
PS_sales = []
PS_dates = []
index_PS2 = []
PS2_sales = []
PS2_dates = []
index_PS3 = []
PS3_sales = []
PS3_dates = []
index_PS4 = []
PS4_sales = []
PS4_dates = []

count = 0
for f in df['Platform']:
    if f == 'PS':
        index_PS.append(count)
        try:
            PS_sales.append(int(df['NA_Sales'][count]))
            PS_dates.append(int(df['Year'][count]))
        except:
            pass
    elif f == 'PS2':
        index_PS2.append(count)
        try:
            PS2_sales.append(int(df['NA_Sales'][count]))
            PS2_dates.append(int(df['Year'][count]))
        except:
            pass
    elif f == 'PS3':
        index_PS3.append(count)
        try:
            PS3_sales.append(int(df['NA_Sales'][count]))
            PS3_dates.append(int(df['Year'][count]))
        except:
            pass
    elif f == 'PS4':
        index_PS4.append(count)
        try:
            PS4_sales.append(int(df['NA_Sales'][count]))
            PS4_dates.append(int(df['Year'][count]))
        except:
            pass
    count += 1
print(PS_dates)

plt.figure(1, tight_layout=True)

plt.plot(PS_dates, PS_sales, color='green', marker='*', markersize=10, linestyle='--', alpha=0.5, label="PS")
plt.plot(PS2_dates, PS2_sales, color='red', marker='*', markersize=10, linestyle='--', alpha=0.5, label='PS2')
plt.plot(PS3_dates, PS3_sales, color='blue', marker='*', markersize=10, linestyle='--', alpha=0.5, label='PS3')

x_ticks = [x for x in range(1980, 2018)]
y_ticks = [y for y in range(0,50)]
print(x_ticks)

plt.axis([1980, 2018, 0, 50])  # [xmin, xmax, ymin, ymax]
plt.xticks(x_ticks, year_numbers, rotation=45)  # replaces the shown values on the graph axis

plt.title("CTA Usage")
plt.xlabel("Year", color='red', fontsize=20)
plt.ylabel("Usage")
plt.legend()
plt.show()
