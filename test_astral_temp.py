from astral import LocationInfo, sun
import datetime
#from astral.sun import sun
import pandas as pd

# city = LocationInfo("Los_Angeles", "America", "America/Los_Angeles", 47.61, 122.33)
# s = sun(city.observer, date=datetime.date(2015, 10, 12))
# print((
#     f'Dawn:    {s["dawn"]}\n'
#     f'Sunrise: {s["sunrise"]}\n'
#     f'Noon:    {s["noon"]}\n'
#     f'Sunset:  {s["sunset"]}\n'
#     f'Dusk:    {s["dusk"]}\n'
# ))

# city2 = LocationInfo(47.61, 122.33)
# s2 = sun(city2.observer, date=datetime.date(2015, 10, 12))
# print((
#     f'Dawn:    {s2["dawn"]}\n'
#     f'Sunrise: {s2["sunrise"]}\n'
#     f'Noon:    {s2["noon"]}\n'
#     f'Sunset:  {s2["sunset"]}\n'
#     f'Dusk:    {s2["dusk"]}\n'
# ))

# print(city.tzinfo)
# print(city2.tzinfo)

#generate some abitrary timestamp to put into series
d = {}
counter = 0
for i in range(10):
    sunrise = pd.Timestamp('2015-10-06T07082' + str(counter))
    d[counter] = sunrise
    counter += 1

sunrise = pd.Series(data = d)
print(sunrise)
print( (sunrise.dt.tz_localize("America/Los_Angeles") - pd.to_datetime(sunrise.dt.date).dt.tz_localize("America/Los_Angeles")) )


# print("=-----=-=-=-")
# print(pd.to_datetime(sunrise.dt.date).dt.tz_localize('America/Los_Angeles'))
# print(sunrise - pd.to_datetime(sunrise.dt.date))#.dt.total_seconds() / (60 * 60)


listOfDays = ['2015-10-14', '2015-10-11', '2015-10-15','2015-10-07','2015-10-16','2015-10-06','2015-10-20','2015-10-17','2015-10-18','2015-10-19','2015-10-09','2015-10-12','2015-10-13','2015-10-10', '2015-10-08']

import datetime
from astral import LocationInfo, sun
city = LocationInfo(47.61, 122.33)
x = datetime.datetime(2015, 10, 14)
sunrise = sun.sunrise(city.observer, x, tzinfo = city.tzinfo)
print(sunrise)

    