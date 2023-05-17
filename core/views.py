from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.db.models import Count

from .models import *
from .forms import *

@user_passes_test(lambda u: u.customuser.level == 'worker')
def index(request):

    user = request.user
    users = User.objects.exclude(pk=user.pk)
    conversations = []

    for u in users:
        messages_users = Message.objects.filter(
            (Q(sender=user) & Q(addressee=u)) | (Q(sender=u) & Q(addressee=user))
        ).last()

        if messages_users:
            conversations.append(messages_users)

    sorted_list = sorted(conversations, key=lambda x: x.id, reverse=True)
    
    context = {
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'conversations': sorted_list,
        'messages_read': Message.objects.filter(Q(addressee=user, read=False)).count(),
        'user': user,   
    }
    
    return render(request, 'index.html', context)


def talk(request, user2):
    if str(request.method) == 'POST':
        addressee = User.objects.get(id=user2)
        sender = request.user

        form = MessageForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data.get('content')

            new_message = Message(sender=sender, addressee=addressee, content=content)
            new_message.save()

            return redirect('talk', user2=user2)

    else:

        user = request.user
        users = User.objects.exclude(pk=user.pk)
        conversations = []

        for u in users:
            messages_users = Message.objects.filter(
                (Q(sender=user) & Q(addressee=u)) | (Q(sender=u) & Q(addressee=user))
            ).last()

            if messages_users:
                conversations.append(messages_users)

        sorted_list = sorted(conversations, key=lambda x: x.id, reverse=True)
    
        messages_users = Message.objects.filter(
            (Q(sender=user) & Q(addressee=user2)) | (Q(sender=user2) & Q(addressee=user))
        ).order_by('-id')

        context = {
            'services': Service.objects.all(),
            'projects': Project.objects.all(),
            'conversations': sorted_list,
            'messages_read': Message.objects.filter(Q(addressee=user, read=False)).count(),
            'user': user,

            'messages': messages_users,
            'user2': User.objects.filter(id=user2),

            'form' : MessageForm(),
        }
        
        return render(request, 'talk.html', context)
