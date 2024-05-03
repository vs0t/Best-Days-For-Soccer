import requests
import tkinter as tk
from tkinter import scrolledtext, Frame
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_weather(city, state):
    url = "https://visual-crossing-weather.p.rapidapi.com/forecast"
    querystring = {
        "aggregateHours": "1",
        "location": f"{city},{state},USA",
        "contentType": "json",
        "unitGroup": "us",
        "shortColumnNames": "false",
    }
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def analyze_weather(data):
    best_times = {"Good": [], "Great": [], "Best": [], "All": []}
    for location, location_data in data["locations"].items():
        for forecast in location_data["values"]:
            temp = forecast.get("temp")  # Use .get() to safely access dictionary values
            conditions = forecast.get("conditions", "").lower()
            pop = forecast.get("pop", 0)
            humidity = forecast.get("humidity", 100)  # Default to 100 if humidity is None

            if temp is not None and ("clear" in conditions or "partially cloudy" in conditions) and (65 <= temp <= 85) and (0 <= pop <= 10) and humidity < 60:
                datetime_obj = datetime.strptime(forecast["datetimeStr"], "%Y-%m-%dT%H:%M:%S%z")
                date_str = datetime_obj.strftime("%A, %B %d, %Y at %I:%M %p")
                quality = "Good"
                if temp > 75:
                    quality = "Great"
                if temp > 75 and humidity < 50:
                    quality = "Best"
                
                entry = f"{date_str} - {temp}°F, Humidity: {humidity}%, Conditions: {conditions.title()}, Quality: {quality}"
                best_times["All"].append(entry)
                if quality in best_times:
                    best_times[quality].append(entry)

    return best_times

def display_results(quality="All"):
    results = weather_data.get(quality, [])
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "\n".join(results) if results else "No ideal days found for this category.")

def get_best_times():
    global weather_data
    city = city_entry.get()
    state = state_entry.get()
    data = fetch_weather(city, state)
    weather_data = analyze_weather(data)
    display_results("All")  # Show all results initially
    filter_buttons_frame.pack(fill="x", padx=10, pady=10)  # Show buttons after search

# GUI Layout
root = tk.Tk()
root.title("Best Soccer Times Finder")
root.geometry("600x400")

input_frame = Frame(root)
input_frame.pack(pady=10, padx=10, fill="x")

tk.Label(input_frame, text="Enter City:").pack(side="left", padx=10)
city_entry = tk.Entry(input_frame, width=15)
city_entry.pack(side="left", padx=10)

tk.Label(input_frame, text="Enter State Code (e.g., SC):").pack(side="left", padx=10)
state_entry = tk.Entry(input_frame, width=5)
state_entry.pack(side="left", padx=10)

tk.Button(input_frame, text="Get Best Times", command=get_best_times).pack(side="left", padx=10)

result_text = scrolledtext.ScrolledText(root, height=10, width=50, wrap=tk.WORD)
result_text.pack(padx=10, pady=10, fill="both", expand=True)

filter_buttons_frame = Frame(root)
tk.Button(filter_buttons_frame, text="Show All", command=lambda: display_results("All")).pack(side="left", expand=True)
tk.Button(filter_buttons_frame, text="Show Good", command=lambda: display_results("Good")).pack(side="left", expand=True)
tk.Button(filter_buttons_frame, text="Show Great", command=lambda: display_results("Great")).pack(side="left", expand=True)
tk.Button(filter_buttons_frame, text="Show Best", command=lambda: display_results("Best")).pack(side="left", expand=True)

root.mainloop()
