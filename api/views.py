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
        converter = []
        checker = []
        for dest in data["languages"]:
            print(dest["value"])
            print(data)
            translator = Translator()
            translation = translator.translate(chunk, dest=dest["value"])
            converter.append(translation.text)
            print(translation.text)

            blob = TextBlob(translation.text)
            try:
                final = blob.translate(from_lang=dest["value"], to='en')
                checker.append(str(final))
            except NotTranslated:
                checker.append(str(translation.text))
        routes = {
            "Translation": converter,
            "Cross Check": checker,
        }
        # print(LANGUAGES)
        return JsonResponse(routes, safe=False)


def languages(request):
    if request.method == "GET":
        return JsonResponse({"language": LANGUAGES}, safe=False)
