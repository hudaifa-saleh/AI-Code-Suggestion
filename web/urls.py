from django.urls import path
from . import views


urlpatterns = [
    path("", views.code_start, name="home"),
    path("suggest/", views.code_suggestion, name="suggest"),
    path("old", views.old_code, name="old"),
    path("delete_old/<old_id>", views.delete_old_code, name="delete_old"),
]
