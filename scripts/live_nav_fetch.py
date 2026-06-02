import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print("Status Code:", response.status_code)

print("\nResponse Text:")
print(response.text[:1000])