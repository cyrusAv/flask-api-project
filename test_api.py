
import requests

BASE_URL = "http://127.0.0.1:5001"

# Test 1: GET /hello
response = requests.get(f"{BASE_URL}/hello", timeout=5)
print("GET /hello")
print("Status:", response.status_code)
print("Response:", response.json())
assert response.status_code == 200

# Test 2: GET /data
response = requests.get(f"{BASE_URL}/data", timeout=5)
print("\nGET /data")
print("Status:", response.status_code)
print("Response:", response.json())
assert response.status_code == 200

# Test 3: POST /data
new_item = {
    "name": "Java",
    "category": "Programming"
}

response = requests.post(
    f"{BASE_URL}/data",
    json=new_item,
    timeout=5
)
print("\nPOST /data")
print("Status:", response.status_code)
print("Response:", response.json())
assert response.status_code == 201

# Test 4: Verify the new item exists
response = requests.get(f"{BASE_URL}/data", timeout=5)
items = response.json()

assert any(
    item["name"] == "Java" for item in items
)

print("\nAll API tests passed!")
