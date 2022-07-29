""" translator contains functions to translate English to French """

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path, override=True)

api_key = os.environ.get('apikey')
authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
)
url = os.environ['url']
language_translator.set_service_url(url)

def english_to_french(string):
    """Translate string in English into string in French."""
    if not string:
        return ''

    translation = language_translator.translate(
            text=string,
            model_id='en-fr'
            ).get_result()
    return translation["translations"][0]["translation"]

def french_to_english(string):
    """Translate string in French into string in English."""
    if not string:
        return ''
    translation = language_translator.translate(
            text=string,
            model_id='fr-en',
            ).get_result()
    return translation["translations"][0]["translation"]
