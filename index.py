from requests import post
from auth_key import auth_key

url = 'https://api-free.deepl.com/v2/translate'
auth_key = auth_key()

get_request_params = lambda auth_key, text, source_lang, target_lang: {
    'auth_key': auth_key,
    'text': text,
    'source_lang': source_lang,
    'target_lang': target_lang,
    'alternative_translations': 1
}

def translate_deepl(url, params):
    response = post(url, data=params)
    if response.status_code == 200:
        response_json = response.json()
        for translation in response_json['translations']:
            print(translation['text'])
    else:
        print(f'Request failed with status code: {response.status_code}')

text = 'Hola mundo hermoso'
source_lang = 'ES'
target_lang = 'EN'

params= get_request_params(auth_key, text, source_lang, target_lang)
translate_deepl(url, params)
