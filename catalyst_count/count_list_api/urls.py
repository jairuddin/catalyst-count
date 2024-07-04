from django.urls import path
from .views import *

urlpatterns = [
    path('filter/', FilterCountView.as_view(), name = 'filter')
]

