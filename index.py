from auth_key import auth_key

from functions import get_request_params, translate_deepl

# Define la dirección URL de la API de Deepl
url = 'https://api-free.deepl.com/v2/translate'
auth_key = auth_key()

languages = [
    (1, 'ES', 'Spanish'),
    (2, 'EN', 'English'),
    (3, 'DE', 'German'),
    (4, 'FR', 'French'),
    (5, 'IT', 'Italian'),
    (6, 'NL', 'Dutch'),
    (7, 'PL', 'Polish'),
]

other_translation = True
while other_translation:
    print("\nLenguajes disponibles:")
    for idx, language in enumerate(languages):
        print(f"{idx + 1}. {language[2]} ({language[1]})")

    selected_source_lang = int(input("\nSelecciona el número del lenguaje de origen: "))
    selected_target_lang = int(input("Selecciona el número del lenguaje de destino: "))

    source_lang = languages[selected_source_lang - 1][1]
    target_lang = languages[selected_target_lang - 1][1]

    text = input("Ingresa el texto a traducir: ")
    
    params = get_request_params(auth_key, text, source_lang, target_lang)
    translate_deepl(url, params)

    other = input("¿Quieres otra traducción? (S/N)")
    while other not in ['s', 'S', 'n', 'N']:
        print("Entrada inválida, por favor escribe 's' o 'n'.")
        other = input("¿Quieres otra traducción? (S/N)")

    if other in ['n', 'N']: other_translation = False
