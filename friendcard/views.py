from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from friendcard.models import FriendCard
from friendcard.forms import *

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

class CardDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = FriendCard

    def get(self, request, name):
        """ Returns a specific wiki page by slug. """
        card = self.get_queryset().get(name=name)
        print(card)
        return render(request, 'friendcard/page.html', {
          'card': card
        })

class CardCreateView(CreateView):
  def get(self, request, *args, **kwargs):
      context = {'form': CardCreateForm()}
      return render(request, 'friendcard/new.html', context)

  def post(self, request, *args, **kwargs):
      form = CardCreateForm(request.POST)
      if form.is_valid():
          post = form.save()
          return HttpResponseRedirect(reverse_lazy('card-details-page', args=[post.name]))
      return render(request, 'friendcard/new.html', {'form': form})
