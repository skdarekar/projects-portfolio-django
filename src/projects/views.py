from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
# Create your views here.


def project_home_view(request):
    return render(request, 'home.html', {})


def project_list_view(request):
    query_set = Project.objects.all()
    context = {
        'project_list': query_set
    }
    return render(request, 'projects/project_list.html', context)


def project_add_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        query_set = Project.objects.all()
        context = {
            'project_list': query_set
        }
        return render(request, 'projects/project_list.html', context)

    context = {
        'project_form': form
    }
    return render(request, 'projects/project_add.html', context)
