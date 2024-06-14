from django.urls import path
from . import views


urlpatterns = [
    path("a/", views.CreateAPI.as_view(), name='create_urls')
]
