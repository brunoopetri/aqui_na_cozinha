from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<receita_id>', views.receita, name='receita')
]
