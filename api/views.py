from django.http import JsonResponse
import json
from googletrans import Translator, LANGUAGES
from django.views.decorators.csrf import csrf_exempt
from textblob import TextBlob
from textblob.exceptions import NotTranslated


@csrf_exempt
def translator_func(request):
    if request.method == "POST":
        data = json.loads(request.body)
        chunk = data["name"]
        src = data["inputDest"]['value']
        routes_data = []
        for dest in data["languages"]:
            print(dest["value"])
            print(data)
            translator = Translator()
            translation = translator.translate(chunk, src=src, dest=dest["value"])
            routes_trans = translation.text
            print(translation.text)

            blob = TextBlob(translation.text)
            try:
                final = blob.translate(from_lang=dest["value"], to='en')
                routes_cross_check = str(final)
                print(routes_cross_check)
            except NotTranslated:
                routes_cross_check = str(translation.text)
            routes_data.append({
                "translation": routes_trans,
                "cross_check": routes_cross_check,
                "language": dest["label"]
            })
        routes = routes_data
        # print(LANGUAGES)
        return JsonResponse(routes, safe=False)


def languages(request):
    if request.method == "GET":
        return JsonResponse({"language": LANGUAGES}, safe=False)
