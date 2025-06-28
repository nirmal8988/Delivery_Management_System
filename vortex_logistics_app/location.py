from geopy.geocoders import Nominatim


def get_lat_long(place_name):
    geolocator = Nominatim(user_agent="moki_location", timeout=10)
    location = geolocator.geocode(place_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None


def main():
    place_name = "perundurai"
    coordinates = get_lat_long(place_name)

    if coordinates:
        print(f"Latitude and Longitude of {place_name}: {coordinates}")
    else:
        print(f"Location not found for {place_name}.")


if __name__ == "__main__":
    main()
