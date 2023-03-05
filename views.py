from django.shortcuts import redirect, render
from main.forms import UserRegistration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "main/index.html")

def discussion(request):
    return render(request, "main/forums.html")

def user_registration(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, username+"you account is ready to share stories!")
            return redirect('main:discussion')
    context = { 'form': form }
    return render(request, 'main/register.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:discussion')
        else:
            messages.info(request, 'Username/password is experiencing climate change..')

def user_logout(request):
    logout(request)
    return render(request, 'forum/index.html')
