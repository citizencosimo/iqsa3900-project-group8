from django.urls import path
from . import views

urlpatterns = [
    path('publisher_a', views.CreatePublisher),
    path('add_game', views.CreateGame),
    path('add_genre', views.CreateGenre),
    path('add_language', views.CreateLanguage),
    path('add_developer', views.CreateDeveloper),
    path('add_platform', views.CreatePlatform, name='createplatform'),
    path('update_game', views.UpdateGame),
    path('delete_game', views.DeleteGame),
    path('staff', views.ListView)
]