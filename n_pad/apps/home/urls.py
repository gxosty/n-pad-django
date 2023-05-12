from django.urls import path, include

from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name = "index"),
    path('create_note/', views.create_note, name = "create_note"),
    path('edit_note/<int:note_id>', views.edit_note, name = "edit_note")
]