import requests
from dotenv import load_dotenv
import os
import json



load_dotenv()
TOKEN = os.getenv('OCR_API')

def ocr_space_url(url, overlay=False, api_key=TOKEN, language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'OCREngine': '3',
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

def get_buck_score(url):
    test_url = ocr_space_url(url=url)
    # Parse the JSON response find the int value in the

    text = json.loads(test_url)['ParsedResults'][0]['ParsedText'].splitlines()
    return text[2]

def get_db_score(url):
    test_url = ocr_space_url(url=url)
    # Parse the JSON response find the int value in the

    text = json.loads(test_url)['ParsedResults'][0]['ParsedText'].splitlines()
    print(text)
    return text[9]


