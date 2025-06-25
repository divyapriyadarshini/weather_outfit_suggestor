city_coords = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "paris": (48.8566, 2.3522)
}

def get_coordinates(city_name):
    return city_coords.get(city_name.lower())
