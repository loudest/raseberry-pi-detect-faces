#Get Current Weather
import pyowm
from twilio.rest import TwilioRestClient

def send_sms(humidity, temperature):
	owm = pyowm.OWM('93118b993e65e8f38d1e80ac384b8ebc')  # You MUST provide a valid API key

	# You have a pro subscription? Use:
	# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
	owm = pyowm.OWM(API_key='93118b993e65e8f38d1e80ac384b8ebc', subscription_type='free')
	# Will it be sunny tomorrow at this time in Milan (Italy) ?
	forecast = owm.daily_forecast("Seattle,WA")
	tomorrow = pyowm.timeutils.tomorrow()
	forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

	# Search for current weather in London (UK)
	observation = owm.weather_at_place('seattle,wa,us')
	w = observation.get_weather()
	#print(w)                      # <Weather - reference time=2013-12-18 09:20,
	                              # status=Clouds>

	# Weather details
	temp = w.get_temperature('fahrenheit')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
	wind = w.get_wind()                  # {'speed': 4.6, 'deg': 330}
	status = w.get_status()

	low = temp.get('temp_min')
	hi = temp.get('temp_max')
	# Search current weather observations in the surroundings of
	# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
	#observation_list = owm.weather_around_coords(-22.57, -43.12)

	temp.get('temp')

	#Send Current Weather to Phone
	accountSID = 'AC5683ea1c077e2a08a53daf4ea9d330e7'
	authToken = 'a40390c71bdab192af5e1c78258b5118'
	twilioCli = TwilioRestClient(accountSID, authToken)
	myTwilioNumber = '+14259709504'
	#myCellPhone = '+12532933749'
	myCellPhone = '+15125531488'
	facts="temp:"+str(temperature)+", humidity: "+str(humidity)
	outmessage = 'Argus detected someone.\r\nInside is '+facts+'.\r\nView the live stream here: https://www.twitch.tv/loudest_man'
	#print(outmessage)
	message = twilioCli.messages.create(body=outmessage, from_=myTwilioNumber, to=myCellPhone) #MediaUrl='https://upload.wikimedia.org/wikipedia/commons/c/c7/School_lunch.jpg'

