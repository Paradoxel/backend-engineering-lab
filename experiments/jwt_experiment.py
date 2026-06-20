import json
import base64
import hmac
import hashlib



# Fake user database
users = {
    "Mohmmadreza": {
        "id": 1,
        "password": "1234"
    }
}



# Secret key (server-side only)
SECRET_KEY = "supersecret"



# Helper: Base64 encoding
def base64_encode(data: str) -> str:
    return base64.b64encode(data.encode()).decode()



# Login function (JWT creation)
def login(username, password):
    user = users.get(username)

    # user validation
    if not user:
        return None

    if password != user["password"]:
        return None

    
    # JWT HEADER 
    header = {
        "alg": "HS256",
        "typ": "JWT"
    }

    
    # JWT PAYLOAD 
    payload = {
        "user_id": user["id"],
        "role": "admin"
    }

    
    # Convert to JSON
    header_json = json.dumps(header)
    payload_json = json.dumps(payload)

    
    # Base64 encoding
    header_base64 = base64_encode(header_json)
    payload_base64 = base64_encode(payload_json)

    
    # SIGNATURE (HMAC SHA256)
    
    signature = hmac.new(
        SECRET_KEY.encode(),
        payload_base64.encode(),
        hashlib.sha256
    ).hexdigest()

    
    # FINAL JWT STRUCTURE (almost real)
    jwt_token = f"{header_base64}.{payload_base64}.{signature}"

    return jwt_token



# Test
print(login("Mohmmadreza", "1234"))



def parse_jwt(token:str):
    # split jwt to 3 parts
    parts=token.split('.')
    if len(parts)!=3:
        return None;

    header_b64 = parts[0]
    payload_b64 = parts[1]
    signature = parts[2]

    return {
        "header": header_b64,
        "payload": payload_b64,
        "signature": signature
    }

print(parse_jwt(login("Mohmmadreza", "1234")))



def verify_jwt(token:str):
    parsed=parse_jwt(token)
    if not parsed:
        return False

    payload_b64 = parsed["payload"]
    signature = parsed["signature"]

    # Recompute signature
    expected_signature = hmac.new(
        SECRET_KEY.encode(),
        payload_b64.encode(),
        hashlib.sha256
    ).hexdigest()

    # Compare signatures
    if expected_signature != signature:
        return False

    return True


print(verify_jwt(login("Mohmmadreza", "1234")))