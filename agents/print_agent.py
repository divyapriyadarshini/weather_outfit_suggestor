class PrintAgent:
    
    def display_final_message(self, city, temperature, suggestion, rain_advice):
        print(f"\n[Final Output]")
        print(f"The current temperature in {city.title()} is {temperature}°C.")
        print(f"Recommended outfit: {suggestion}")
        print(f"{rain_advice}")
