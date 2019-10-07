from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
