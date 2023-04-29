from django.urls import path

from .views import CodeAnalizer

urlpatterns = [
    path('code/', CodeAnalizer.as_view(), name='code'),
]
