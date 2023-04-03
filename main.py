import requests

# API anahtarınız OpenWeatherMap API
api_key = "your_api_key_here"


city = input("Hangi şehrin hava durumunu öğrenmek istiyorsunuz? ")


url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


response = requests.get(url)

if response.status_code == 200:

    data = response.json()
    

    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    

    print(f"{city} şehrinde hava {description}, sıcaklık {temperature} derece, nem oranı {humidity}%")
else:

    print("Hata: Şehir bulunamadı")
