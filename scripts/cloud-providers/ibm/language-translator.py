# install ibm_watson package
# !pip install ibm_watson wget


from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

url = ""
iam_apikey = ""
lt_version="2018-05-01" # set the language translator version

text="Hello there! Hope you are good?"

authenticator = IAMAuthenticator(iam_apikey)
language_translator = LanguageTranslatorV3(authenticator=authenticator, version=lt_version)
language_translator.set_service_url(url)

# get list of languages
languages = language_translator.list_identifiable_languages().get_result()

# print languages in a tabular form
normalized_languages = json_normalize(languages, "languages")
print(normalized_languages)

# translate from english (en) to french (fr)
translation_response = language_translator.translate(text=text, model_id='en-fr').get_result()
parsed_response = translation_response['translations'][0]['translation']
print(parsed_response)