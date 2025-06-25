import requests

class WeatherAgent:
    
    def get_weather(self, city):
        coords = self.get_coordinates_from_mcp(city)
        if not coords:
            print(f"[WeatherAgent] City '{city}' not found.")
            return None
        
        lat, lon = coords
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

        try:
            resp = requests.get(url)
            resp.raise_for_status()
            data = resp.json()
            temp_c = data["current_weather"]["temperature"]
            rain_mm = data["current_weather"].get("precipitation", 0)
            print(f"[WeatherAgent] Current temperature in {city.title()}: {temp_c}°C")
            print(f"[WeatherAgent] Precipitation in {city.title()}: {rain_mm} mm")
            return temp_c, rain_mm
        except Exception as e:
            print(f"[WeatherAgent] API Error: {e}")
            return None

    def get_coordinates_from_mcp(self, city):
        try:
            response = requests.post("http://localhost:8000/context", json={
                "query": f"coordinates for {city}"
            })
            coords = response.json().get("context")
            return tuple(coords) if coords else None
        except:
            print("[WeatherAgent] MCP not reachable.")
            return None
