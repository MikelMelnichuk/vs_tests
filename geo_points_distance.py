import geopy.distance

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="mikel_test")

yaniv_6 = geolocator.geocode("Yaniv 6, Petah Tikva, Israel")
print(yaniv_6.address)

home = geolocator.geocode("Добролюбова 25, Москва")
print(home.address)


yaniv_coords = (yaniv_6.latitude, yaniv_6.longitude)
home_coords = (home.latitude, home.longitude)
print(f"{geopy.distance.geodesic(yaniv_coords, home_coords).km} KM from home")
