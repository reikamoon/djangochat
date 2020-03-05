from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from friendcard.models import FriendCard
from api.serializers import FriendCardSerializer
# Create your views here.
class FriendCardList(APIView):
    def get(self, request):
        card = FriendCard.objects.all()[:20]
        data = FriendCardSerializer(card, many=True).data
        return Response(data)
