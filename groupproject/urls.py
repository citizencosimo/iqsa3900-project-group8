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
    path('upload/', views.image_upload_view, name='image_upload'),

    #Individual Views
    path('view_developer/<int:pk>', views.ViewDeveloper, name='developer_view'),
    path('view_game/<int:pk>', views.ViewGame, name='game_view'),
    path('view_genre/<int:pk>', views.ViewGenre, name='genre_view'),
    path('view_language/<int:pk>', views.ViewLanguage, name='language_view'),
    path('view_platform/<int:pk>', views.ViewPlatform, name='platform_view'),
    path('view_publisher/<int:pk>', views.ViewPublisher, name='publisher_view'),

    #CRUD Add
    path('publisher_a', views.CreatePublisher, name='add_publisher'),
    path('add_game', views.CreateGame, name='add_game'),
    path('add_genre', views.CreateGenre, name='add_genre'),
    path('add_language', views.CreateLanguage, name='add_language'),
    path('add_developer', views.CreateDeveloper, name='add_developer'),
    path('add_platform', views.CreatePlatform, name='add_platform'),

    #CRUD Update and Delete
    path('update_game/<int:pk>', views.UpdateGame, name='update_game'),
    path('delete_game/<int:pk>', views.DeleteGame, name='delete_game'),
    path('update_publisher/<int:pk>', views.UpdatePublisher, name='update_publisher'),
    path('delete_publisher/<int:pk>', views.DeletePublisher, name='delete_publisher'),
    path('update_developer/<int:pk>', views.UpdateDeveloper, name='update_developer'),
    path('delete_developer/<int:pk>', views.DeleteDeveloper, name='delete_developer'),
    path('update_platform/<int:pk>', views.UpdatePlatform, name='update_platform'),
    path('delete_platform/<int:pk>', views.DeletePlatform, name='delete_platform'),
    path('update_genre/<int:pk>', views.UpdateGenre, name='update_genre'),
    path('delete_genre/<int:pk>', views.DeleteGenre, name='delete_genre'),
    path('update_language/<int:pk>', views.UpdateLanguage, name='update_language'),
    path('delete_language/<int:pk>', views.DeleteLanguage, name='delete_language'),

    #Review Include
    path('review/', include('reviewertools.urls')),
] 