import json
from meteo_company_client import MeteoCompanyClient

LATITUDE=<<your latitude>>
LONGITUDE=<<your longitude>>

mc = MeteoCompanyClient(LATITUDE, LONGITUDE)

def rain(request):
    rain_list = mc.rain_list
    return json.dumps([rain.value for rain in rain_list])