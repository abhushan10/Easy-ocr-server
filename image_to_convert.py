import json
import base64 , requests
from json.decoder import JSONDecodeError
image_encoded = ''
with open("1.png", "rb") as imageFile:
    image_encoded = base64.b64encode(imageFile.read())
    base64_img = image_encoded.decode('utf-8')
url = 'http://0.0.0.0:8080/admin/{}'.format(base64_img)
try:
    requests.post(url)
except:
    print('[!] Opps. Cannot make connection..!! -_-')
class Extract_Json_Command:
    def Json_to_string():
        try:
            response = requests.get("http://0.0.0.0:8080/bot")
            cmd_json_parsed = json.loads(response.text)
            extracted_command = "{}".format(cmd_json_parsed['Text-From-Image'])
            if extracted_command != "":
                    return extracted_command
        except requests.exceptions.ConnectionError:
            pass
        except JSONDecodeError:
            pass
print(Extract_Json_Command.Json_to_string() + '\n======= Coded By : ABHUSHAN ========\n ======= Country : Nepal =======')
