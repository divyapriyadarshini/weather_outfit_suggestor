def suggest_outfit(temperature_c):
    if temperature_c < 10:
        return "Wear a warm jacket and scarf."
    elif temperature_c < 20:
        return "Light jacket or sweater recommended."
    else:
        return "No need for jackets, sweaters or anything."
