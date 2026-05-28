## Requests (REST client)

```python
import requests
```

Set base url and headers:
```python
base_url = 'http://localhost:5000'
req_headers = {'Content-Type': 'application/json'}
```

POST request (CREATE resource):

```python
print('sending POST request')
json_data = {'name': 'Product One', 'price': 12}
result = requests.post(
    url=base_url+'/member',
    json=json_data,
    headers=req_headers
)
if result.status_code == 201:
    print("data received", result.text)
else:
    print("request error", result.status_code, result.text)
```

GET request (READ resource)

```python
print('sending GET request')
result = requests.get(
    url=base_url+'/member/1',
    headers=req_headers
)
if result.status_code == 200:
    print("data received", result.text)
else:
    print("request error", result.status_code, result.text)
```

PUT request (UPDATE resource)

```python
print('sending PUT request')
json_data = {'name': 'Product One Updated', 'price': 13}
result = requests.put(
    url=base_url+'/member/1',
    json=json_data,
    headers=req_headers
)
if result.status_code == 200:
    print("data received", result.text)
else:
    print("request error", result.status_code, result.text)
```

Delete request (DELETE resource)

```python
print('sending DELETE request')
result = requests.delete(
    url=base_url+'/member/1',
    headers=req_headers
)
if result.status_code == 200:
    print("data received", result.text)
else:
    print("request error", result.status_code, result.text)
```

**References:** [request params](https://www.w3schools.com/python/ref_requests_get.asp)