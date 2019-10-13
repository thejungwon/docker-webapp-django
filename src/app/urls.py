from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('pizzak/', views.pizzas, name='pizzas'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/profile/', views.profile, name='profile'),
    path('pizzalist/', views.pizzalist, name='pizzalist'),
    path('account/myorders/', views.myorders, name='myorders')
]
