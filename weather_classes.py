import requests


class Conditions():
    def __init__(self, zip):
        self.zip = zip

    def get_conditions(zip):
        conditions = requests.get('http://api.wunderground.com/api/b4bcce775639916a/conditions/q/28387.json')
        your_town = conditions.json()['current_observation']['display_location']['full']
        precip = conditions.json()['current_observation']['precip_today_string']
        return your_town, precip


class Forecast():
    def __init__(self, zip):
        self.zip = zip

    def get_forecast(zip):
        forecast = requests.get('http://api.wunderground.com/api/b4bcce775639916a/forecast10day/q/28387.json')
        day = []
        for each in forecast.json()['forecast']['simpleforecast']['forecastday']:
            day.append("Low: " + each['low']['fahrenheit'] + "   High: " + each['high']['fahrenheit'] + "   and " + each['icon'])
        return day


class SunriseSunset():
    def __init__(self, zip):
        self.zip = zip

    def get_sunrise_sunset(zip):
        astronomy = requests.get('http://api.wunderground.com/api/b4bcce775639916a/astronomy/q/28387.json')
        sunrise = astronomy.json()['sun_phase']['sunrise']['hour'] + ":" + astronomy.json()['sun_phase']['sunrise']['minute'] + " am"
        sunset = astronomy.json()['sun_phase']['sunset']['hour'] + ":" + astronomy.json()['sun_phase']['sunset']['minute'] + " pm"
        return sunrise, sunset


class Alerts():
    def __init__(self, zip):
        self.zip = zip

    def get_alerts(zip):
        alerts = requests.get('http://api.wunderground.com/api/b4bcce775639916a/alerts/q/28387.json')
        if not alerts.json()['alerts']:
            local_alerts = "There are no alerts for your area."
        else:
            local_alerts = alerts.json()['alerts']
        return local_alerts


class Hurricanes():
    def __init__(self, zip):
        self.zip = zip

    def get_hurricanes(zip):
        hurricanes = requests.get('http://api.wunderground.com/api/b4bcce775639916a/currenthurricane/q/28387.json')
        canes = []
        for i in range(len(hurricanes.json()['currenthurricane'])):
            canes.append(hurricanes.json()['currenthurricane'][i]['stormInfo']['stormName_Nice'])
        return canes
