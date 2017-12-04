import requests
from urllib.parse import quote

def sendwa(my_apikey,message,destination):
    api_url = "http://panel.apiwha.com/send_message.php"
    api_url += "?apikey="+quote(my_apikey)
    api_url += "&number="+quote(destination)
    api_url += "&text="+quote(message)
    r=requests.get(api_url)
    print(r.text)
    return

def receivewa(my_apikey):
    api_url = "http://panel.apiwha.com/get_messages.php"
    api_url += "?apikey="+quote(my_apikey)
    api_url += "&type=IN"
    api_url += "&markaspulled=1";
    api_url += "&getnotpulledonly=1";
    r=requests.get(api_url)
    # print(r.text)
    return r.text





# sendwa("IJBVEB2W820EA6OQD1O7","Hello World!!","5491161889205")
# receivewa("IJBVEB2W820EA6OQD1O7")
