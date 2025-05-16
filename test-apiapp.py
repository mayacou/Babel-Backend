import requests

response = requests.post(
    "https://mayacou-babel-router-api.hf.space/translate",
    json={"text": "Hello, how are you?", "target_lang": "fr"},
    timeout=60
)

print(response.status_code)
print(response.json())
