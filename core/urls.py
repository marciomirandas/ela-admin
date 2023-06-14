from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(index), name='index'),
    path('conversa/<int:user2>/', login_required(talk), name='talk'),   
    path('nova-mensagem/', login_required(new_message), name='new_message'),   
]