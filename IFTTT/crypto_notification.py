import requests
import time
from datetime import datetime

API_URL = 'https://api.coinmarketcap.com/v1/ticker/{}/?convert=HKD'
TARGET = 'ethereum'
# Some possible id for cryptocurrency at coinmarketcap api:
# bitcoin
# ethereum
# ripple
# bitcoin-cash
# litecoin
# See doc at API page: https://coinmarketcap.com/api/
INTERVAL_SEC = 600 # 10 minute
HISTORY_SIZE = 6 # every hour
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/dfJfqGUK6VsXREemjgJMc-'

def get_latest_crypto_price_hkd(crypto_id):
	# send request get response in json
	url = API_URL.format(crypto_id)
	response = requests.get(url)
	response_json = response.json()
	# parsing
	name = response_json[0]['name']
	price = float(response_json[0]['price_hkd']) # converting price to float
	return name, price

def post_ifttt_webhook(event, value1, value2):
	# building payload and url
	ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
	data = {'value1': value1, 'value2': value2}
	# sending POST to webhook URL
	requests.post(ifttt_event_url, json=data)

def format_price_history(history):
	rows = []
	for entry in history:
		# formats the date into a string: '2018-03-19 13:40'
		date = entry['date'].strftime('%Y-%m-%d %H:%M')
		price = entry['price']
		# <b> (bold) tag creates bolded text
		row = '{}: HK$<b>{}</b>'.format(date, price)
		rows.append(row)

	# <br> is for new line
	return '<br>'.join(rows)

def main():
	price_history = []
	while True:
		name, price = get_latest_crypto_price_hkd(TARGET)
		date = datetime.now()
		price_history.append({'date': date, 'price': price})
		
		# send notification to IFTTT
		# post_ifttt_webhook('crypto_price_notification', name, 'HK${}'.format(price))
		
		# send price update to telegram once we have enough 
		if len(price_history) == HISTORY_SIZE:
			post_ifttt_webhook('crypto_price_update', name, format_price_history(price_history))
			# reset history
			price_history = []

		time.sleep(INTERVAL_SEC)	

if __name__ == '__main__':
	main()