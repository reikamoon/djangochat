from django.urls import path
from . import views
from accounts.views import SignUpView

urlpatterns = [
    path('new', SignUpView.as_view(), name = 'signup')
]
