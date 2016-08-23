import re
from weather_classes import *


while True:
    print("\n"*60)
    entry = input("From what zipcode would you like to see the weather ?    ")
    if re.match(r'\d{5}', entry) or re.match(r'\d{5}-\d{4}', entry):
        your_town, precip = Conditions.get_conditions(entry)
        days = Forecast.get_forecast(entry)
        sunrise, sunset = SunriseSunset.get_sunrise_sunset(entry)
        local_alerts = Alerts.get_alerts(entry)
        canes = Hurricanes.get_hurricanes(entry)
        break

print("\n"*60)
print("In " + your_town + " they had rainfall in the amount of: " + precip)
print("The sun rose/will rise today, at ", sunrise, "and set at ", sunset)
print("Local Alerts are as follows:   ", local_alerts, "\n")
print("The forecast for the the next 10 days is as follows: ")
for idx, each in enumerate(days):
    print("Day ", idx, ": ", each)
print("\n\n")
print("In addition, there are ", len(canes), " hurricanes across the globe, and their names are:\n")
for each in canes:
    print(each, "  |  ", end="")
print("\n"*5)

# 83469
