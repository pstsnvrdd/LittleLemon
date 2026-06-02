from django.urls import path
from .views import *

urlpatterns = [
    path('menu-items', MenuView.as_view()),
    path('menu-items/<int:pk>', MenuDetailView.as_view()),
    path('message/', msg),
]