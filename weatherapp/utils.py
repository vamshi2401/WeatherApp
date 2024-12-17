import requests

def get_weather(city):
  API_KEY='c29499293210a6a962089f8ab683c071'
  URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
  response = requests.get(URL)
  if response.status_code == 200:
      return response.json()
  else:
      return None
  
  