# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import pandas as pd

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon


cities = []
def cityreader(cities=[]):
  f = open('src/cityreader/cities.csv', 'r')
  f.close()

  df = pd.read_csv('src/cityreader/cities.csv')
  cities1 = [(df.city[i], df.lat[i],df.lng[i]) for i in range(len(df.city))]
  cities = [City(cities1[i][0], cities1[i][1], cities1[i][2]) for i in range(len(cities1))]
  
  return cities


# Get latitude and longitude values from the user
lat1, lon1 = input("Enter Lat1, Lon1: " ).split(",")
lat2, lon2 = input("Enter Lat2, Lon2: " ).split(",")
lat1 = int(lat1)
lat2 = int(lat2)
lon1 = int(lon1)
lon2 = int(lon2)

cit = cityreader(cities)

def lat_between(lat1,lat2, cit):
  if lat1 < lat2:
    h= []
    for a in range(len(cit)):      
      if lat1 < cit[a].lat < lat2:
        h.append(cit[a].lat)
    return h
  else:
    h= []
    for a in range(len(cit)):      
      if lat1 > cit[a].lat > lat2:
        h.append(cit[a].lat)
    return h


def lon_between(lon1,lon2, cit):
  if lon1 < lon2:
    w= []
    for a in range(len(cit)):      
      if lon1 < cit[a].lon < lon2:
        w.append(cit[a].lat)
    return w
  else:
    w= []
    for a in range(len(cit)):      
      if lon1 > cit[a].lon > lon2:
        w.append(cit[a].lat)
    return w

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

latitudes = lat_between(lat1,lat2,cit)
latitudes2 = lon_between(lon1,lon2,cit)

markers = intersection(latitudes,latitudes2)

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  for b in markers:
    for a in range(len(cit)):
      if b == cit[a].lat:
        within.append(cit[a])
  return within
 
print(cityreader_stretch(lat1, lon1, lat2, lon2, cit))

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)



# Get latitude and longitude values from the user
lat1, lon1 = input("Enter Lat1, Lon1: " ).split(",")
lat2, lon2 = input("Enter Lat2, Lon2: " ).split(",")
lat1 = int(lat1)
lat2 = int(lat2)
lon1 = int(lon1)
lon2 = int(lon2)
#cit = cityreader(cities)
'''
def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  # within = []
  for a in range(len(cit)):
    if lon1 < lon2:
      if lon1 < cit[a].lon < lon2:
        print((cit[a].name, cit[a].lat, cit[a].lon))

    else:
      if lon2 < cit[a].lon <= lon1:
        print((cit[a].name, cit[a].lat, cit[a].lon))

  within = cityreader_stretch(lat1, lon1, lat2, lon2, cit)
  return within
  
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

#  return within'''