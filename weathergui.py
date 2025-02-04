import requests
import mysql.connector
import tkinter as tk
from tkinter import messagebox


class WeatherDashboard:
    def __init__(self, api_key, db_config):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.db_config = db_config
        self.connect_db()

    def connect_db(self):
        """Establish connection to the MySQL database."""
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            self.create_table()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def create_table(self):
        """Create table for storing search history."""
        query = """
        CREATE TABLE IF NOT EXISTS search_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            city_name VARCHAR(255),
            temperature FLOAT,
            humidity INT,
            weather_condition VARCHAR(255),
            search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_weather(self, city):
        """Fetch weather data for a given city."""
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "weather_condition": data["weather"][0]["description"],
            }
            self.store_search_history(weather_data)
            return weather_data
        else:
            return {"error": "City not found or API error occurred."}

    def store_search_history(self, weather_data):
        """Store weather data in the database."""
        query = """
        INSERT INTO search_history (city_name, temperature, humidity, weather_condition)
        VALUES (%s, %s, %s, %s)
        """
        values = (
            weather_data["city"],
            weather_data["temperature"],
            weather_data["humidity"],
            weather_data["weather_condition"],
        )
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_search_history(self):
        """Retrieve search history from the database."""
        query = "SELECT city_name, temperature, humidity, weather_condition, search_time FROM search_history ORDER BY search_time DESC"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_db(self):
        """Close the database connection."""
        self.cursor.close()
        self.conn.close()


API_KEY = "a022478e6e6052140c51d731f1408d22"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Vsr2622003*",
    "database": "db1",
}


class WeatherAppGUI:
    def __init__(self, root, dashboard):
        self.root = root
        self.dashboard = dashboard
        self.root.title("Weather Dashboard")
        self.root.geometry("500x400")

        self.city_label = tk.Label(root, text="Enter City Name:")
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root)
        self.city_entry.pack(pady=5)

        self.fetch_button = tk.Button(
            root, text="Fetch Weather", command=self.fetch_weather
        )
        self.fetch_button.pack(pady=20)

        self.weather_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.weather_label.pack(pady=10)

        self.history_button = tk.Button(
            root, text="View Search History", command=self.view_history
        )
        self.history_button.pack(pady=10)

    def fetch_weather(self):
        """Fetch weather data based on user input and update the display."""
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        weather = self.dashboard.fetch_weather(city)

        if "error" in weather:
            messagebox.showerror("Error", weather["error"])
        else:

            self.weather_label.config(
                text=f"Weather in {city}:\n"
                f"Temperature: {weather['temperature']}°C\n"
                f"Humidity: {weather['humidity']}%\n"
                f"Condition: {weather['weather_condition']}"
            )

    def view_history(self):
        """Show the weather search history in a new window."""
        history_window = tk.Toplevel(self.root)
        history_window.title("Search History")
        history_window.geometry("600x400")

        history = self.dashboard.get_search_history()

        if not history:
            messagebox.showinfo("History", "No search history found.")
            return

        history_listbox = tk.Listbox(history_window, width=80, height=15)
        history_listbox.pack(pady=20)

        for record in history:
            history_listbox.insert(
                tk.END,
                f"City: {record[0]}, Temp: {record[1]}°C, Humidity: {record[2]}%, "
                f"Condition: {record[3]}, Time: {record[4]}",
            )


if __name__ == "__main__":

    dashboard = WeatherDashboard(API_KEY, DB_CONFIG)

    root = tk.Tk()

    app = WeatherAppGUI(root, dashboard)

    root.mainloop()

    dashboard.close_db()
