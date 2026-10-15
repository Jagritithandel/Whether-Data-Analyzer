weather_data=(
    ("Delhi",35,40),
    ("Mumbai",32,70),
    ("Jaipur",38,30),
    ("Chennai",34,65),
    ("Shimla",22,55),
)
print("==== Weather Data Analyzer ====")
print("CITY\t\tTEMPERATURE(°C)\t\tHUMIDITY(%)")
print("-"*50)
for city, temp, humidity in weather_data:
    print(f"{city}\t\t{temp}\t\t\t{humidity}")
hottest=max(weather_data, key=lambda x: x[1])
coldest=min(weather_data, key=lambda x: x[1])
sorted_weather=sorted(weather_data, key=lambda x: x[1])
print("\nHottest City:", hottest[0], "with temperature", hottest[1], "°C")
print("Coldest City:", coldest[0], "with temperature", coldest[1], "°C")
print("\nCities sorted by temperature:")
for city, temp, humidity in sorted_weather:
    print(f"{city}:  {temp}°C  ,Humidity:{humidity}%\n")