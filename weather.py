import requests
import mysql.connector


class WeatherDashboard:
    def __init__(self, api_key, db_config):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.db_config = db_config
        self.connect_db()

    def connect_db(self):

        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            self.create_table()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def create_table(self):

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

        query = "SELECT city_name, temperature, humidity, weather_condition, search_time FROM search_history ORDER BY search_time DESC"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_db(self):

        self.cursor.close()
        self.conn.close()


API_KEY = "a022478e6e6052140c51d731f1408d22"
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Vsr2622003*",
    "database": "db1",
}


if __name__ == "__main__":
    dashboard = WeatherDashboard(API_KEY, DB_CONFIG)

    while True:
        print("\nWeather Dashboard")
        print("1. Fetch Weather by City")
        print("2. View Search History")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather = dashboard.fetch_weather(city)
            if "error" in weather:
                print(weather["error"])
            else:
                print(f"\nWeather in {city}:")
                print(f"Temperature: {weather['temperature']}°C")
                print(f"Humidity: {weather['humidity']}%")
                print(f"Condition: {weather['weather_condition']}")

        elif choice == "2":
            history = dashboard.get_search_history()
            print("\nSearch History:")
            for record in history:
                print(
                    f"City: {record[0]}, Temperature: {record[1]}°C, Humidity: {record[2]}%, Condition: {record[3]}, Time: {record[4]}"
                )

        elif choice == "3":
            dashboard.close_db()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
