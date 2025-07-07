import csv
import matplotlib.pyplot as plt 

dates = []
openPrice = []
highest = []
lowest = []
closePrice = []
volumes = []

with open('aapl.csv')as file:
    reader = csv.reader(file)
    for date, Open, high, low, close, volume in reader:
        dates.append(date)
        openPrice.append(Open)
        highest.append(high)
        lowest.append(low)
        closePrice.append(close)
        volumes.append(volume.replace(",", ""))

years = []
monthes = []
days = []
terms = []

for i in range(len(dates)):
    date_sep = dates[i].split("/")
    year = int(date_sep[2])
    month = int(date_sep[0])
    day = int(date_sep[1])
    years.append(year)
    monthes.append(month)
    days.append(day)
    term = (years[i] - 2024) * 365 + (monthes[i] - 1) * 31 + days[i]
    terms.append(term)

ups = []
downs = []
closePrices = []
openPrices = []
highesPrices = []
lowestPrices = []
intvolumes = []


for j in range(len(closePrice)):
    finish = float(closePrice[j])
    openPrices.append(float(openPrice[j]))
    closePrices.append(finish)
    highesPrices.append(float(highest[j]))
    lowestPrices.append(float(lowest[j]))
    intvolumes.append(int(volumes[j]))
    if closePrices[j] >= closePrices[j-1]:
        up = closePrices[j] - closePrices[j-1]
        ups.append(up)
        
    else:
        down = closePrices[j-1] - closePrices[j]
        downs.append(down)

