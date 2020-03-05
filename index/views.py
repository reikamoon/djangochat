from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template

# Create your views here.
def IndexView(request):
    user = None
    auth = request.user.is_authenticated
    if auth:
        user = request.user
    return render(request, 'index/index.html', {'user': user})
