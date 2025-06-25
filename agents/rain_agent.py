class RainAgent:
    
    def rain_advice(self, rain_mm):
        if rain_mm > 0:
            advice = "It might rain. Carry an umbrella!"
        else:
            advice = "No rain expected. Umbrella not needed."
        
        print(f"[RainAgent] {advice}")
        return advice
