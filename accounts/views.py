from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import CreateUserForm


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password = password)
                messages.success(request,f'با موفقیت وارد شدید!')

                if user is not None:
                    login(request, user)
                    return redirect('accounts:profile')
            
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required(login_url="/accounts/login")
def logout_view(request):
    logout(request)
    messages.success(request,'با موفقیت خارج شدید!')
    return redirect('/')




def signup_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'حساب شما با موفقیت ساخته شد!')
            return redirect('accounts:profile')


    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


@login_required(login_url="/accounts/login")
def profile_view(request):
    return render(request, 'accounts/profile.html')

