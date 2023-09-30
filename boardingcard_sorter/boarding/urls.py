# boarding/urls.py
from django.urls import path
from .views import BoardingCardSortView

urlpatterns = [
    path('boarding-cards/', BoardingCardSortView.as_view(), name='boarding-card-list'),
]
