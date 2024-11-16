import requests
import json

def invoke_lambda(api_gateway_url, payload):
    headers = {'Content-Type': 'application/json'}
    try:
        #response = requests.post(api_gateway_url, data=json.dumps(payload), headers=headers) # UNCOMMENT THIS LINE
        response = requests.post(url=api_gateway_url, json=payload, headers=headers)
        print(f"Raw response: {response.text}") # ADD THIS LINE
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error invoking Lambda function: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

# ... rest of your code ...

# API GatewayエンドポイントURL
api_gateway_url = "https://i86xwtbmre.execute-api.ap-northeast-1.amazonaws.com/default/docker-selenium-lambda-kansuke"

# リクエストペイロード (必要に応じて)
payload = {
  "key1": "https://www.google.com/",
  "key2": "value2",
  "key3": "value3"
}
# Lambda関数呼び出し
result = invoke_lambda(api_gateway_url, payload)

if result:
    print(f"Lambda function response: {result}")
    


