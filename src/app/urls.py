from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path(_('pizzak/'), views.pizzas, name='pizzas'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
