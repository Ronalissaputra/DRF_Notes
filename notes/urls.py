from django.urls import path
from .views import Notes_list


urlpatterns = [path("notes/", Notes_list, name="notes-list")]
