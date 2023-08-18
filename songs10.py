import requests  as rq
import clipboard as pc

# checking if api key exists in the data.txt file
with open("data.txt", "r+") as data:
	api_key = data.read()
	if api_key=="":
		api_key = str(input('Enter rapid api key: '))
		open("data.txt", "w").write(api_key)


# settingv params for requests
url = "https://billboard-api2.p.rapidapi.com/hot-100"
querystring = {"date":"2019-05-11","range":"1-10"}
headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "billboard-api2.p.rapidapi.com"
}

response = rq.get(url, headers=headers, params=querystring).json()

try: 
	print(f"""\n--------- Today's Top Hits ---------\n\nDate: {response["info"]["date"]}\n""")
	
	i = 1
	while 1:
		try: 
			print(f'{i}. {response["content"][str(i)]["title"]} by {response["content"][str(i)]["artist"]}')
		except KeyError:
			break
		i+=1

except KeyError:
	print(response["message"]) 
