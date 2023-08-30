
import requests
import sys
data = sys.argv
response = requests.get(
    "https://v6.exchangerate-api.com/v6/65e670cd69369c639aeeffe5/latest/USD")
fetch = response.json()
rate = fetch['conversion_rates']
if data[2] in fetch['conversion_rates'] and data[3] in fetch['conversion_rates']:
    tousd = float(data[1]) / rate[data[2]]
    result = tousd * rate[data[3]]
    print(result)
else:
    print("Invalid request")
