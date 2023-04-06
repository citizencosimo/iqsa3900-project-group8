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
    path('', views.DatabaseLinks, name='database_links')

]