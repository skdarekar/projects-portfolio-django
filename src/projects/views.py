from django.shortcuts import render

# Create your views here.
def project_home_view(request):
    return render(request, 'home.html', {});

def project_list_view(request):
    return render(request, 'projects/project_list.html', {});

def project_add_view(request):
    return render(request, 'projects/project_add.html', {});