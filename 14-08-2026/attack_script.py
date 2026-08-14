import requests

url = "http://127.0.0.1:8000/"

# for i in range(1000):
#     response = requests.get(url)
#     print(f"Request {i + 1}: {response.status_code}")

# # post request 
data = {"name": "John", "age": 30}
for i in range(100000000000):
    response = requests.post(url, json=data)
    print(f"Request {i + 1}: {response.status_code}, Response: {response.json()}")


# azure - microsoft cloud - 200+ services
# aws - amazon web services - 200+ services
# gcp - google cloud platform - 200+ services

#  for how much data goes out of the service ( egress) - 5GB free per month, then pay for it