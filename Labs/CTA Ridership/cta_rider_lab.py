'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''
#The usage of the cta has slowly decreased over time. However there has been a steeper decline in bus usage which is nearly balanced out by a mild increase in rail usage.
#The explanation of this could be that Chicago has improved its rail system over the last decade and thus people have been more inclined to use it and have optted out of using the bus.
import csv
import matplotlib.pyplot as plt

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

print(data)

print("data")
data.pop(0)
years = [x[0] for x in data]
bus = [int(x[1]) for x in data]
rail = [int(x[3]) for x in data]
total = [int(x[4]) for x in data]

year_numbers = years[-10:]
rail = rail[-10:]
bus = bus[-10:]
total = total[-10:]
print(year_numbers)
print(bus)
print(rail)
print(total)

plt.figure(1, tight_layout=True)

plt.plot(year_numbers, rail, color='green', marker='*', markersize=10, linestyle='--', alpha=0.5, label="Rail")
plt.plot(year_numbers, bus, color='red', marker='*', markersize=10, linestyle='--', alpha=0.5, label='Bus')
plt.plot(year_numbers, total, color='blue', marker='*', markersize=10, linestyle='--', alpha=0.5, label='Total')


plt.axis([-1, 10, 0, 750000000])  # [xmin, xmax, ymin, ymax]
plt.xticks(year_numbers, year_numbers, rotation=45)  # replaces the shown values on the graph axis

plt.title("CTA Usage")
plt.xlabel("Year", color='red', fontsize=20)
plt.ylabel("Usage")
plt.legend()
plt.show()

