import requests

PIXELA_ENDPOINT="https://pixe.la/v1/users"

TOKEN="ChurchOfAustrianPainter"
USERNAME="mastercheif1"

user_params={"token":TOKEN,
             "username":USERNAME,
             "agreeTermsOfService":"yes",
             "notMinor":"yes",
             "thanksCode":"ThisIsThanksCode"}

response=requests.post(
    url=PIXELA_ENDPOINT,
    json=user_params
)
print(response.json())

graph_endpoint=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID="graph1"
headers={"X-USER-TOKEN":TOKEN}
graph_params={
    "id":GRAPH_ID,
    "name":"pythonGraph",
    "type":"int",
    "unit":"seconds",
    "color":"ajisai"
}


response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
print(response.json())
