import re
import requests
import time

class Rain:
    def __init__(self, forecast):
        self._epoch = int(re.search(r'\d+', forecast['TimeStampUTC']).group(0))
        self._value = float(forecast['Value'])

    @property
    def epoch(self):
        return self._epoch

    @property
    def value(self):
        return self._value


class MeteoCompanyClient:
    def __init__(self, lat, lon):
        self._uri = 'https://api120.themeteocompany.com/precipitation/getforecastbylatlon/?lat={}&lon={}'.format(lat, lon)

    @property
    def rain_list(self):
        self.update()
        return self._rain_list

    def update(self):
        current_time = int(time.time() * 1000) 
        forecasts=requests.get(self._uri).json()['ForecastResult']

        rain_list = [Rain(forecast) for forecast in forecasts]
        rain_future = [rain for rain in rain_list if rain.epoch > current_time]

        self._rain_list = rain_future
