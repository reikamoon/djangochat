from django.urls import path

from api.views import FriendCardList

urlpatterns = [
    path('cards/', FriendCardList.as_view(), name='cards_list'),
]
