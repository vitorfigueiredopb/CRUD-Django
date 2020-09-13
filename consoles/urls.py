from django.urls import path
from .views import ListConsoles, CreateConsole, UpdateConsole, DeleteConsole

urlpatterns = [
    path('', ListConsoles.as_view(), name='list_consoles'),
    path('create_console/', CreateConsole.as_view(), name='create_console'),
    path('update_console/<int:pk>', UpdateConsole.as_view(), name='update_console'),
    path('delete_console/<int:pk>', DeleteConsole.as_view(), name='delete_console')
]