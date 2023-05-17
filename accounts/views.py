from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

from .forms import LoginForm

# Página de login
def login(request):
    if str(request.method) == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            authenticated = authenticate(username=username, password=password)

            if authenticated:
                try:
                    if(authenticated.customuser.level == 'worker'):
                        auth_login(request, authenticated)
                        return redirect('index')
                    elif(authenticated.customuser.level == 'client'):
                        auth_login(request, authenticated)
                        return redirect('index')   
                except:
                    messages.error(request, 'Este usuário não tem permissão para entrar!')
                    return redirect('login')
            else:
                messages.error(request, 'Usuário e/ou Senha incorretos!')
                return redirect('login')
                 
        else:       
            return render(request, 'login.html', context)

    else:
    
        form = LoginForm()
        context = {
            'form': form,
        }       
        return render(request, 'login.html', context)
        

# Sair do sistema
def logout(request):
    auth_logout(request)
    return redirect('login')
