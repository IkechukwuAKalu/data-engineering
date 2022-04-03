# install ibm_watson package
# !pip install ibm_watson wget


from ibm_watson import SpeechToTextV1 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

url = ""
iam_apikey = ""
filename="path/to/file.mp3"

authenticator = IAMAuthenticator(iam_apikey)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url)

recognized_data = None

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type="audio/mp3")
    recognized_data = response.result["results"]

normalized = json_normalize(recognized_data, "alternatives")    
print(normalized)