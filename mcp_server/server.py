from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import uvicorn

app = FastAPI()

@app.post("/context")
async def get_context(request: Request):
    data = await request.json()
    query = data.get("query")

    if query and query.startswith("coordinates for "):
        city = query.replace("coordinates for ", "").strip()
        coords = get_coordinates_from_api(city)
        if coords:
            return {"context": coords}
        else:
            return {"context": None}
    
    return {"context": "Unknown query"}

def get_coordinates_from_api(city):
    url = f"https://nominatim.openstreetmap.org/search?city={city}&format=json"
    try:
        response = requests.get(url, headers={"User-Agent": "WeatherOutfitSuggester/1.0"})
        response.raise_for_status()
        results = response.json()
        if results:
            lat = float(results[0]["lat"])
            lon = float(results[0]["lon"])
            return [lat, lon]
        else:
            return None
    except Exception as e:
        print(f"[MCP] Error fetching coordinates: {e}")
        return None

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
