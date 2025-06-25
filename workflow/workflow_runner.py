from agents.weather_agent import WeatherAgent
from agents.outfit_agent import OutfitAgent
from agents.rain_agent import RainAgent
from agents.print_agent import PrintAgent

def run_workflow():
    weather_agent = WeatherAgent()
    outfit_agent = OutfitAgent()
    rain_agent = RainAgent()
    print_agent = PrintAgent()

    print("\n=== Weather & Outfit Suggestion System ===")

    city = input("Enter city name (Delhi, Mumbai, New York, London, Paris): ").strip()
    weather = weather_agent.get_weather(city)

    if weather is None:
        print("Workflow terminated due to invalid city or API error.")
        return

    temperature, rain_mm = weather
    suggestion = outfit_agent.get_suggestion(temperature)
    rain_advice = rain_agent.rain_advice(rain_mm)

    print_agent.display_final_message(city, temperature, suggestion, rain_advice)
