#from conversion_functions import *
import sys

if (sys.argv[1] == "feet"):
    feet = float(sys.argv[2])
    furlongs = feetToFurlongs(feet)
    print(f"Furlongs: {furlongs}")

if (sys.argv[1] == "pounds"):
    pounds = float(sys.argv[2])
    firkins = poundsToFirkins(pounds)
    print(f"Firkins: {firkins}")

if (sys.argv[1] == "days"):
    days = float(sys.argv[2])
    fortnights = daysToFortnights(days)
    print(f"Fortnights: {fortnights}")
    
