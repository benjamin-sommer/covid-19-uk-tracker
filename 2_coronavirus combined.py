#!/usr/bin/env LC_ALL=en_US.UTF-8 /usr/local/bin/python3
#
# <bitbar.title>Coronavirus Tracker 2</bitbar.title>
# <bitbar.version>v2.0</bitbar.version>
# <bitbar.desc>It tracks Coronavirus cases</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
#
# by benjamin-sommer

try:
  import requests
except ImportError:
  print("Need to install requests module")
  print("Type the following:")
  print("pip install requests")

import json

url = 'https://corona.lmao.ninja/v2/countries/uk'
r = requests.get(url)
uk = r.json()

pic = int(round(float(uk["todayCases"]) / (float(uk["cases"]) - float(uk["todayCases"])) * 100))
pid = int(round(float(uk["todayDeaths"]) / (float(uk["deaths"]) - float(uk["todayDeaths"])) * 100))

print(u"🇬🇧 Cases: " + str(uk["cases"]) + " (" + u"\u001b[32m" + u"\u2191" + str(pic) + "%" + u"\u001b[0m" + ")" + "  Deaths: " + str(uk["deaths"]) + " (" + u"\u001b[32m" + u"\u2191" + str(pid) + "%" + u"\u001b[0m" + ")")

print("---")

url = 'https://corona.lmao.ninja/v2/countries'
r = requests.get(url)
countries = r.json()

todayCases= 0
todayDeaths = 0

totalCases= 0
totalDeaths = 0

for country in countries:
    todayCases += country["todayCases"]
    todayDeaths += country["todayDeaths"]

    totalCases += country["cases"]
    totalDeaths += country["deaths"]

pic = int(round(float(todayCases) / (float(totalCases) - float(todayCases)) * 100))
pid = int(round(float(todayDeaths) / (float(totalDeaths) - float(todayDeaths)) * 100))

print(":earth_americas: Cases: " + str(totalCases) + " (" + u"\u001b[32m" + u"\u2191" + str(pic) + "%" + u"\u001b[0m" + ")" + "  Deaths: " + str(totalDeaths) + " (" + u"\u001b[32m" + u"\u2191" + str(pid) + "%" + u"\u001b[0m" + ")" )
