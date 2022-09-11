import requests
import datetime as dt
USERNAME = "nutamy"
TOKEN = "Z26SgOItjzmtaR)PX%R"
GRAPH_ID = "pythonyellow"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Python coding",
    "unit": "commit",
    "type": "int",
    "color": "ichou"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
now = dt.datetime.now()
today = now.strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "10"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantity": "4"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"


## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)