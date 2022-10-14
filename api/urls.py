from django.urls import path
from .views import translator_func, languages


urlpatterns = [
    path('', translator_func),
    path('language', languages)
]
