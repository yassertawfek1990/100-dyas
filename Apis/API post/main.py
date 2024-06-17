import requests
from datetime import datetime,timedelta

# first step create user
token = "12a1d2bhbjhbgvfds5aa0)"
username = "yassertawfek"
domian = "https://pixe.la/v1/users"
parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=domian,json=parameters)
# response.raise_for_status()
# print(response.text)


# second step create a graph
header = { # it is required to provide the token
    "X-USER-TOKEN": token
    }

graph_domain = f"{domian}/{username}/graphs"

graph_id  = "pthon-graph1"
graph_parameters = {
    "id": graph_id,
    "name": "python",
    "type": "float",
    "unit": "hour",
    "color": "momiji"

}

# response_graph = requests.post(url=graph_domain,json=graph_parameters,headers=header)
# print(response_graph.text)

# third step add data to the graph

the_domain = f"{graph_domain}/{graph_id}"
date = datetime.now().date()

d = datetime.strftime(date, '%Y%m%d')
pixels_params = {
    "date": d,
    "quantity": input("how many hours did we study?\n")
}

# print(the_domain)

# response_pixel = requests.post(url=the_domain,json=pixels_params,headers=header)
# print(response_pixel.text)

yesterday = date - timedelta(days=1)
y = datetime.strftime(yesterday, '%Y%m%d')
put_domain = f"{the_domain}/{y}"
put_params = {
    "quantity": "99.5"
}

# response_put = requests.put(url=put_domain,json=put_params,headers=header)
# print(response_put.text)

delete_domain = f"{the_domain}/{d}"
deleting = requests.delete(url=delete_domain,headers=header)
print(deleting.text)
