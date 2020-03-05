from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from friendcard.models import FriendCard

# Create your views here.
class CardListView(ListView):
    """ Renders a list of all Pages. """
    model = FriendCard

    def get(self, request):
        """ GET a list of Pages. """
        cards = self.get_queryset().all()
        return render(request, 'friendcard/list.html', {
          'cards': cards,
        })
