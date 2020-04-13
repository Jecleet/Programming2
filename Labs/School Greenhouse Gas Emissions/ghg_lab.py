
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts)
- Create a best fit line for schools shown. (5pts)


Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
'''
import csv
import numpy as np
import matplotlib.pyplot as plt

with open("Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)

titles = data.pop(0)
print(titles)
area_idx = titles.index("Gross Floor Area - Buildings (sq ft)")
emission_idx = titles.index("Total GHG Emissions (Metric Tons CO2e)")
property_idx = titles.index("Primary Property Type")

data_usable = []
for item in data:
    try:
        float(item[emission_idx])
        float(item[area_idx])
        if item[property_idx] == "K-12 School":
            if item[0] == "2018":
                data_usable.append(item)
    except:
        pass
print(data_usable)


area = [float(school[area_idx]) for school in data_usable]
emissions = [float(school[emission_idx]) for school in data_usable]
names = [school[2] for school in data_usable]
parker_idx = names.index("Francis W Parker School")

plt.figure("Total GHG Emmissions v building square footage", figsize=(10, 6))  # add figsize
plt.annotate("Francis W Parker", xy= (area[parker_idx], emissions[parker_idx]))
plt.scatter(area, emissions)
plt.ylabel("GHG Emissions")
plt.xlabel("Building Square Footage")
plt.title("Total GHG Emmissions vs. building square footage")

m, b = np.polyfit(area, emissions, 1)
area2 = np.array(area)
plt.plot(area2, m*area2 + b, c= 'red')
plt.show()