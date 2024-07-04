from django.urls import path
from .views import *

urlpatterns = [
    path('query/',FilterFormView.as_view(), name='query')
]