# Weather & Outfit Suggestor (Multi-Agent System with Rain Feature & MCP)

This project implements a multi-agent system that suggests appropriate outfits based on real-time weather conditions, including rain probability. It demonstrates integration with a custom MCP (Model Context Provider) server to fetch city coordinates, following principles of the Agent2Agent (A2A) ecosystem.

## Features

- Multi-agent workflow with:
  - **Weather Agent:** Fetches real-time temperature
  - **Rain Agent:** Checks for rain probability
  - **Suggestor Agent:** Recommends outfit based on weather & rain
- MCP server provides city coordinates using OpenStreetMap API
- Clean, modular project structure
- Uses free public APIs
- Command-line interaction

## Technologies Used

- Python
- FastAPI (for MCP server)
- OpenStreetMap Nominatim API (for coordinates)
- Open-Meteo API (for weather & rain probability)
- Modular agent design

## How It Works

The user inputs a city name.  
The MCP server fetches the coordinates for that city.  
The Weather Agent uses those coordinates to get real-time temperature.  
The Rain Agent checks rain probability for the location.  
The Suggestor Agent recommends suitable clothing based on temperature and rain conditions.  

## How to Run

### 1. Setup

git clone https://github.com/divyapriyadarshini/weather_outfit_suggestor.git <br>
cd weather_outfit_suggestor <br>
python3 -m venv .venv <br>
source .venv/bin/activate <br>
pip install -r requirements.txt <br>

#### 2. Run MCP Server (Separate Terminal)
cd mcp_server <br>
python server.py <br>

### 3. Run Main Workflow
In another terminal:
source .venv/bin/activate <br>
python executor.py <br>


Follow the prompts to input a city name and receive outfit suggestions based on real-time weather and rain conditions.
