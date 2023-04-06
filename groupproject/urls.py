from django.urls import path
from . import views

urlpatterns = [
    path('publisher_a', views.CreatePublisher),
    path('add_game', views.CreateGame),
    path('add_genre', views.CreateGenre),
    path('add_language', views.CreateLanguage),
    path('add_developer', views.CreateDeveloper),
    path('add_platform', views.CreatePlatform, name='createplatform'),
    path('update_game/<int:pk>', views.UpdateGame, name='update_game'),
    path('delete_game/<int:pk>', views.DeleteGame, name='game_delete'),
    path('view_game/<int:pk>', views.ViewGame, name='game_view'),
    path('staff', views.ListView),
    path('games', views.GameList, name="game_list"),
]