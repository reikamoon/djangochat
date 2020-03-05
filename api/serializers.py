from rest_framework.serializers import ModelSerializer
from friendcard.models import FriendCard

class FriendCardSerializer(ModelSerializer):
    class Meta:
        model = FriendCard
        fields = '__all__'
