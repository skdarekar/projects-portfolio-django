from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages;
from .form import SignUpForm

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

def register_user(request):

    if(request.method == "POST"):
        form = SignUpForm(request.POST);
        if(form.is_valid()):
            user = form.save();
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password);
            login(request, user);
            messages.success(request, ("Registration successful!"))
            return redirect('/projects')
    else:
        form = SignUpForm();
    if(form.errors):
        print(form.errors)
    return render(request, 'authenticate/register_user.html', {
        'form': form
    });
        
def forgot_password_user(request):
    if(request.method == "POST"):
        #TODO - Add logic to handle reset password here
        return redirect('/users/login');
    else:
        return render(request, 'authenticate/password_reset.html', {});