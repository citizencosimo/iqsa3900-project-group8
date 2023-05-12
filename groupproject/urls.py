from django.urls import path, include
from . import views

urlpatterns = [
    #Database top
    path('', views.DatabaseLinks, name='database_links'),

    #List views:
    path('developers', views.DeveloperList, name="developer_list"),
    path('games/', views.GameList, name='game_list'),
    path('genres/', views.GenreList, name='genre_list'),
    path('languages/', views.LanguageList, name='language_list'),
    path('platforms', views.PlatformList, name="platform_list"),
    path('publishers', views.PublisherList, name="publisher_list"),

    #Individual Views
    path('view_developer/<int:pk>', views.ViewDeveloper, name='developer_view'),
    path('view_game/<int:pk>', views.ViewGame, name='game_view'),
    path('view_genre/<int:pk>', views.ViewGenre, name='genre_view'),
    path('view_language/<int:pk>', views.ViewLanguage, name='language_view'),
    path('view_platform/<int:pk>', views.ViewPlatform, name='platform_view'),
    path('view_publisher/<int:pk>', views.ViewPublisher, name='publisher_view'),

    #CRUD Add
    path('add_publisher', views.CreatePublisher, name='add_publisher'),
    path('add_game', views.CreateGame, name='add_game'),
    path('add_genre', views.CreateGenre, name='add_genre'),
    path('add_language', views.CreateLanguage, name='add_language'),
    path('add_developer', views.CreateDeveloper, name='add_developer'),
    path('add_platform', views.CreatePlatform, name='add_platform'),
    path('update_game/<int:pk>', views.UpdateGame, name='update_game'),
    path('delete_game/<int:pk>', views.DeleteGame, name='delete_game'),
    path('view_game/<int:pk>', views.ViewGame, name='game_view'),
    path('games', views.GameList, name="game_list"),
    path('update_publisher/<int:pk>', views.UpdatePublisher, name='update_publisher'),
    path('delete_publisher/<int:pk>', views.DeletePublisher, name='delete_publisher'),
    path('view_publisher/<int:pk>', views.ViewPublisher, name='publisher_view'),
    path('publishers', views.PublisherList, name="publisher_list"),
    path('update_developer/<int:pk>', views.UpdateDeveloper, name='update_developer'),
    path('delete_developer/<int:pk>', views.DeleteDeveloper, name='delete_developer'),
    path('view_developer/<int:pk>', views.ViewDeveloper, name='developer_view'),
    path('developers', views.DeveloperList, name="developer_list"),
    path('update_platform/<int:pk>', views.UpdatePlatform, name='update_platform'),
    path('delete_platform/<int:pk>', views.DeletePlatform, name='delete_platform'),
    path('view_platform/<int:pk>', views.ViewPlatform, name='platform_view'),
    path('platforms', views.PlatformList, name="platform_list"),
    path('', views.DatabaseLinks, name='database_links'),
    path('games/', views.GameList, name='game_list'),
    path('review/', include('reviewertools.urls')),
    path('genres/', views.GenreList, name='genre_list'),
    path('view_genre/<int:pk>', views.ViewGenre, name='genre_view'),
    path('update_genre/<int:pk>', views.UpdateGenre, name='update_genre'),
    path('delete_genre/<int:pk>', views.DeleteGenre, name='delete_genre'),
    path('languages/', views.LanguageList, name='language_list'),
    path('view_language/<int:pk>', views.ViewLanguage, name='language_view'),
    path('update_language/<int:pk>', views.UpdateLanguage, name='update_language'),
    path('delete_language/<int:pk>', views.DeleteLanguage, name='delete_language'),
]