try:
    print("test")
    print(world)
except Exception as error:
    print(error)

import requests
result = None
for i in range(50):
    try:
        result = requests.get("http://worldtimeapi.org/api/ip")
        result = result.json()
        break
    except Exception as error:
        pass
    
print(result)
print(result["client_ip"])

for i in result:
    print(f"{i}:{result[i]}")