from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages;
# Create your views here.
def login_user(request):
    if(request.method == "POST"):
        username = request.POST['username'];
        password = request.POST['password'];
        user = authenticate(request, username=username, password=password);
        if user is not None:
            login(request, user=user);
            return redirect('/projects');
        else:
            messages.success(request, ("Failed to login, please check your credentials and try again!"))
            return redirect('/users/login');
    else:
        return render(request, 'authenticate/login.html', {});

def logout_user(request):
    logout(request);
    messages.success(request, ("Logged out!"))
    return redirect('/users/login')