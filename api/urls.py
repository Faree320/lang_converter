from django.urls import path
from .views import translator_func, languages, language_detector


urlpatterns = [
    path('', translator_func),
    path('language', languages),
    path('detector', language_detector)
]
