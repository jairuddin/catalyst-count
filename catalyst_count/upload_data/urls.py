from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout_view, name='logout_view'), 

]
