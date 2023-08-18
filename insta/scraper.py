import json
import requests


# checking if api key exists in the data.txt file
with open("data.txt", "r+") as data:
	api_key = data.read()
	if api_key=="":
		api_key = str(input('Enter rapid api key: '))
		open("data.txt", "w").write(api_key)


# setting params for requests
url = "https://instagram-bulk-profile-scrapper.p.rapidapi.com/clients/api/ig/ig_profile"

querystring = {"ig":str(input("Enter insta username: ")),"response_type":"short","corsEnabled":"false"}

headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "instagram-bulk-profile-scrapper.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring).json()


print(f"""
-------------------------------------------------------------------\n
Username : {response[0]["username"]}
Full Name : {response[0]["full_name"]}
Follower Count : {response[0]["follower_count"]}
Following Count : {response[0]["following_count"]}

Media Count : {response[0]["media_count"]}

Bio : {response[0]["biography"]}
Bio Links : {response[0]["bio_links"]}

Private : {response[0]["is_private"]}
Business : {response[0]["is_business"]}
Professional : {response[0]["is_professional"]}
New to Instagram : {response[0]["is_new_to_instagram"]}

Profile Pic URL : {response[0]["profile_pic_url"]}\n
HD Profile Pic URL : {response[0]["profile_pic_url_hd"]}\n
-------------------------------------------------------------------
""")