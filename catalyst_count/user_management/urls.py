from django.urls import path
from .views import *


urlpatterns = [
    path('list/', user_list, name='user_list'),
    path('delete/<int:user_id>/', user_delete, name='user_delete'),
    path('add/', add_user, name='add_user'),
]
