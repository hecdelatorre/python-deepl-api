from requests import post

get_request_params = lambda auth_key, text, source_lang, target_lang: {
    'auth_key': auth_key,
    'text': text,
    'source_lang': source_lang,
    'target_lang': target_lang,
    'alternative_translations': 1
}

def translate_deepl(url, params):
    # Realiza la solicitud a la API
    response = post(url, data=params)
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtiene la respuesta de la API
        response_json = response.json()
        # Recorre las traducciones alternativas
        for translation in response_json['translations']:
            # Imprime la traducción alternativa
            print(f'\nTranslation: {translation["text"]}\n')
    else:
        # Imprime el código de estado de la respuesta
        print(f'Request failed with status code: {response.status_code}')
