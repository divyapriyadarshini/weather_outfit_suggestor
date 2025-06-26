
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

```bash
git clone https://github.com/divyapriyadarshini/weather_outfit_suggestor.git
cd weather_outfit_suggestor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run MCP Server (Separate Terminal)

```bash
cd mcp_server
python server.py
```

### 3. Run Main Workflow

In another terminal:

```bash
source .venv/bin/activate
python executor.py
```

Follow the prompts to input a city name and receive outfit suggestions based on real-time weather and rain conditions.

## Project Structure

```
weather_outfit_suggestor/
├── agents/
│   ├── suggestor_agent.py
│   ├── weather_agent.py
│   └── rain_agent.py
├── mcp_server/
│   └── server.py
├── workflow/
│   └── workflow_runner.py
├── executor.py
├── requirements.txt
├── .gitignore
└── README.md
```


