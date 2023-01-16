from temperature import state

temperature_input = float(input("Enter water temperature: "))

water_state = state(temperature_input)
print(water_state)
