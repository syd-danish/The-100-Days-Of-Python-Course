from main import *
import requests
from datetime import datetime

today=datetime.now()
today=today.strftime("%Y%m%d")
pixel_params={
    "date": today,
    "quantity":"200"
}
pixel_address=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
response=requests.post(url=pixel_address,headers=headers,json=pixel_params)
print(response.json())

#--------------update--------------#
update_address=f"{pixel_address}/{today}"
update_params={"quantity":"230"}
response=requests.put(url=update_address,headers=headers,json=update_params)
print(response.json())
#-------------delete----------------#
delete_request=requests.delete(url=pixel_address,headers=headers,json=pixel_params)
print(delete_request.json())
