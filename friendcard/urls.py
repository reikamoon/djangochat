from django.urls import path
from friendcard.views import CardListView


urlpatterns = [
    path('', CardListView.as_view(), name='card-list-page'),
]
