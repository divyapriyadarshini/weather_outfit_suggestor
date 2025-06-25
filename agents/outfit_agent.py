from tools.outfit_selector import suggest_outfit

class OutfitAgent:
    
    def get_suggestion(self, temperature_c):
        suggestion = suggest_outfit(temperature_c)
        print(f"[OutfitAgent] Suggestion based on temperature: {suggestion}")
        return suggestion
