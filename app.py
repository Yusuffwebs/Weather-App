from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "Lqa2LNBsm80l9P0IvU6TgjznWyUc2WIf"  # Your Tomorrow.io API Key

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']

        # Use Tomorrow.io API for weather data
        url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
        response = requests.get(url)
        weather_data = response.json()

        # Handle API errors
        if "code" in weather_data:
            return render_template('index.html', error="City not found or API limit exceeded!")

        # Extract weather information
        weather_info = {
            'city': city,
            'temperature': weather_data['data']['values']['temperature'],  # Temperature in Celsius
            'description': weather_data['data']['values']['weatherCode'],  # Weather code
        }

        return render_template('index.html', weather=weather_info)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
