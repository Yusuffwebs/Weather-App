from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "Lqa2LNBsm80l9P0IvU6TgjznWyUc2WIf"  

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']

        url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
        response = requests.get(url)
        weather_data = response.json()

     
        if "code" in weather_data:
            return render_template('index.html', error="City not found or API limit exceeded!")

      
        weather_info = {
            'city': city,
            'temperature': weather_data['data']['values']['temperature'],  
            'description': weather_data['data']['values']['weatherCode'],  
        }

        return render_template('index.html', weather=weather_info)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
