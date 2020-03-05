from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template
from friendcard.views import CardListView
from friendcard.models import FriendCard

# Create your views here.
class IndexView(generic.ListView):
    model = FriendCard

    def get(self, request):
        """ GET a list of Pages. """
        cards = self.get_queryset().all()
        user = None
        auth = request.user.is_authenticated
        if auth:
            user = request.user
        return render(request, 'index/index.html', {
          'cards': cards,
          'user': user
        })
