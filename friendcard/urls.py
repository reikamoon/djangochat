from django.urls import path
from friendcard.views import CardListView, CardDetailView, CardCreateView


urlpatterns = [
    path('', CardListView.as_view(), name='card-list-page'),
    path('new-card/', CardCreateView.as_view(), name="card-new-page"),
    path('<str:name>/', CardDetailView.as_view(), name='card-details-page'),
]
