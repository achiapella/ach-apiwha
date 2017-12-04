from apiwha import receivewa
from apiwha import sendwa
import json

s = receivewa("IJBVEB2W820EA6OQD1O7")
jdata = json.loads(s)
for d in jdata:
    for key, value in d.items():
        if key=="text":
            texto=value
        if key=="from":
            froms=value
        if key=="to":
            to=value
        # print ("Recibi :",value," del ")
        if key=="creation_date":
            sendwa("IJBVEB2W820EA6OQD1O7","Recibi:"+texto,froms)
        print(key,value)
