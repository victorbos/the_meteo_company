## python function to get results from the precipitation radar ('buienradar') from the_meteo_company
- this appears to be more stable and faster than that of buienradar.nl
- tracked down the calls that are done from their website weerslag.nl to find the api, so this might change in future
- split into a `main.py` and a medule file to make it easily deployable as a function in the google cloud.