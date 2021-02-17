from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('book/<slug:book_slug>', get_by_slug, name='get_by_slug'),
]