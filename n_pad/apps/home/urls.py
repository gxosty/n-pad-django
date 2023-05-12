from django.urls import path, include

from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name = "index"),
    path('edit_note/<int:note_id>', views.edit_note, name = "edit_note")
]